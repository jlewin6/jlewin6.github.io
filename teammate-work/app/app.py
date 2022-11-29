from flask import Flask, render_template, request, redirect, url_for, flash, session
import json 
import os.path
import psycopg2
from flask_socketio import SocketIO, emit


app = Flask(__name__) #Initializer.
app.secret_key = 'randomkey1243424' #for Flash

@app.route('/') #base url
def home():
    #return render_template('home.html', name="Jinja test") #name can be passed to home.html via jinja
    return render_template('home.html') 

@app.route('/about') #introduction page
def about():
    return 'This is introduction page'  #TODO: (Optional)create about.html and create another button to route to introduction page

@app.route('/map', methods=['GET', 'POST']) 
def map():
    if request.method == 'POST':
        # Step 1: Create JSON file and store the recent 5 user inputs (Clinical trials IDs) to nct_inputs.json
        nct_dict = {}
        if os.path.exists('nct_inputs.json'):
            with open('nct_inputs.json') as nct_file:
                nct_dict = json.load(nct_file) #load Json first if exists
        
        user_input = request.form['nct'] 
        
        if user_input in nct_dict.keys():
            flash('NCT ID has recently been used.')
            return redirect(url_for('home')) # When inputs are duplicated, return to home
        
        if len(nct_dict) < 5: #Keep the search history up to 5 in nct_input.json
            nct_dict[user_input] = len(nct_dict)+1 
        else: 
            nct_dict.pop(next(iter(nct_dict)))
            nct_dict[user_input] = list(nct_dict.values())[3]+1 
        
        with open('nct_inputs.json', 'w') as nct_file:
            json.dump(nct_dict, nct_file) #Store user input as JSON
        
        # Step 2: Create small database based on user inqeiry.
        studies_data = get_initial_studydata(user_input)
        # Create sub-table based on study correspond to valid studyIDs
        
        return render_template('map.html', 
                               nct=user_input,
                               nct_dict=nct_dict, #route the user input (NCT#) to map.html via jinja
                               data={'studies' : studies_data}) 
    else: 
        return redirect(url_for('home')) #When approched via GET i.e. http://127.0.0.1:5000/map, return to home

#Helper 1: extract table
def get_initial_studydata(user_input):
    conn = get_connection_object()
    cur = conn.cursor()

    # create a table from database (join columns of interest form multiple table)
    # For now, limit by the most recent 1000 studies
    cur.execute('''
                SELECT c.nct_id, c.name AS name_condition,
                s.overall_status,
                a.name AS name_country,
                i.intervention_id, i.name as name_intervention, 
                b.description
                FROM conditions c
                LEFT JOIN studies s
                ON c.nct_id = s.nct_id
                LEFT JOIN countries a
                ON c.nct_id = a.nct_id
                LEFT JOIN intervention_other_names i
                ON c.nct_id = i.nct_id
                LEFT JOIN brief_summaries b
                ON c.nct_id = b.nct_id
                WHERE c.nct_id is not null AND i.intervention_id is not null    
                
                LIMIT 50000
                ''')
#               ORDER BY nct_id desc #This will slow down the process significanty and seems not stable. 

    
    studies_list = cur.fetchall()
    
    cur.close()
    conn.close()

    mydict = dict()
    for row in studies_list:
        mydict[row[0]] = {"nct_id":row[0],"name_condition":row[1],"overall_status":row[2], 
                          "name_country":row[3],"intervention_id":row[4], 
                          "name_intervention":row[5],"description":row[6]}

    #(Optional) Filter the dictionary based on input: return the list of NCT with the same disease  
    def get_key_from_value(d, val):
        keys = [k for k, v in d.items() if v == val]
        if keys:
            return keys[0]
        return None
    
    subset_dict = dict()
    if user_input in mydict:
        disease = mydict[user_input]['name_condition']
        for v in mydict.values():
            if v['name_condition'] == disease:
                subset_dict[get_key_from_value(mydict, v)] = v                
    else: 
        print("not matched") #TODO: need to implement function to return "no matched NCT IDs"
       
    return json.loads(json.dumps(subset_dict))
    #return json.loads(json.dumps(mydict))


#Helper : connection        
def get_connection_object():
    global conn
    #Connect to AACT dataabase
    conn = psycopg2.connect(database="aact",
                        host="aact-db.ctti-clinicaltrials.org",
                        user="cmuralee3",
                        password="Chithra@91",
                        port="5432")
    return conn

    

@app.route('/<string:nct>') #TODO: Should it be a separate page? or should be a part of /map?
# IDEA: once the calculation is done, redirect to http://127.0.0.1:5000/NCT05565391
def results(nct):
    if os.path.exists('nct_inputs.json'):
        with open('nct_inputs.json') as nct_file:
            nct_json = json.load(nct_file)
            if nct in nct_json.keys():
                return "test1" # TODO: Intead of redirect --> implement db search
   
            
    


# TODO: ADD CSS to make it look nicer