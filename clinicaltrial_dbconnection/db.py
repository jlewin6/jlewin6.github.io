import psycopg2
import json
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def load_home_page():
    studies_data = getInitialStudyData()
    return render_template("home.html", data={'studies' : studies_data})
    
def getInitialStudyData():
    
    conn = getConnectionObject()
    cur = conn.cursor()
    
    cur.execute("Select nct_id, official_title, overall_status from studies order by nct_id asc limit 10000")    
    studies_list = cur.fetchall()
    
    cur.close()
    conn.close()

    mydict = dict()
    for row in studies_list:
        mydict[row[0]] = {"nct_id":row[0],"official_title":row[1],"overall_status":row[2]}
    
    return json.loads(json.dumps(mydict))

@app.route("/countries")
def load_countries_page():
    countries_data = getCountryData()
    return render_template("countries.html", data={'countries' : countries_data}) 
 
def getCountryData():
   
    conn = getConnectionObject()
    cur = conn.cursor()
   
    cur.execute("Select name, count(name) as counts from countries group by name order by counts desc")    
    countries_list = cur.fetchall()
    
    cur.close()
    conn.close()
    
    mydict = dict()
    for row in countries_list:
        mydict[row[0]] = {"name":row[0],"counts":row[1]}

    return json.loads(json.dumps(mydict))

@socketio.on('get_country_details_data')
def getCountryDetailsData(data):

    conn = getConnectionObject()
    cur = conn.cursor()
    
    cur.execute("SELECT gender, count(*) as counts FROM eligibilities where nct_id in (select nct_id from countries where name = '" + data['name'] + "') group by gender order by counts desc")  
    #cur.execute("SELECT * FROM eligibilities limit 1")  
    #field_names = [i[0] for i in cur.description]    
    elegibility_gender_list = cur.fetchall()

    cur.execute("SELECT study_type, count(*) as counts FROM studies where nct_id in (select nct_id from countries where name = '" + data['name'] + "') group by study_type order by counts desc")  
    study_type_list = cur.fetchall() 
    
    cur.close()
    conn.close()
    
    mydict = dict()
    for row in elegibility_gender_list:
        mydict[row[0]] = {"name":row[0],"counts":row[1]}
    genderData = json.loads(json.dumps(mydict))

    mydict = dict()
    for row in study_type_list:
        mydict[row[0]] = {"name":row[0],"counts":row[1]}
    studyTypeData = json.loads(json.dumps(mydict))

    socketio.emit('get_country_details_data_done', {'genderData' : genderData, 'studyTypeData' : studyTypeData})

def getConnectionObject():
    global conn

    conn = psycopg2.connect(database="aact",
                        host="aact-db.ctti-clinicaltrials.org",
                        user="cmuralee3",
                        password="Chithra@91",
                        port="5432")
    return conn

if __name__ == '__main__':
    socketio.run(app)