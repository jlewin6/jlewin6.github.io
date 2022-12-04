import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity

def similarity_score(input):
    # We need to provide a datafram with trial ID's and descriptions
    # ...this is an example with all of the trials that had "stroke" as the condition
    df = pd.read_csv("./data_AACT_united_states_cancer_2000.csv")
    df = df[['nct_id', 'name_condition', 'name_intervention', 'brief_title', 'study_description']]

    # This gives the index of the study that we want to compare the other studies to.
    selected_index= df[df['nct_id'] == input].index[0]
    #selected_index = 10 #This will be replaced to user input
    top_n = 10

    # Descriptions turned into a list
    desc_collection = list(df['brief_title'])
    desc_collection_2 = list(df['study_description'])

    # Creates a vectorizer that will convert descriptions into vectors using idf removing stop words
    vectorizer = TfidfVectorizer(stop_words = text.ENGLISH_STOP_WORDS, use_idf=True)
    X = vectorizer.fit_transform(desc_collection)
    X_2 = vectorizer.fit_transform(desc_collection_2)

    # Finds the cosine similarity between the
    A = np.round_(cosine_similarity(X[selected_index], X), 4)
    A_2 = np.round_(cosine_similarity(X_2[selected_index], X_2), 4)

    # Creates a df of the top n similarity scores
    # Since A is a nested array, we need to use the A[0] to get within it.
    # The last record is the selected record and isn't included
    df_sim_score = pd.DataFrame({'similarity_score_title': np.sort(A[0])[-(top_n+1):]})
    df_sim_score_2 = pd.DataFrame({'similarity_score_description': np.sort(A_2[0])[-(top_n+1):]})

    # Creates a df of the clinical trial records with  the top n similarity scores to
    # the 'selected' trial. The last record is the selected record and isn't included
    df_top_trials = df.iloc[(np.argsort(A[0]))[-(top_n+1):], :].reset_index(drop=True)
    
    # Select columns to display
    df_top_trials = df_top_trials[['nct_id', 'name_condition', 'brief_title', 'study_description']]
    
    # Concatenates the list of trials with the corresponding similiarity scores.
    df_top_w_scores = pd.concat([df_top_trials, df_sim_score, df_sim_score_2], axis=1).sort_values(by=["similarity_score_description"], ascending=False)
    return df_top_w_scores


def similarity_table(input):

    df= similarity_score(input)
    # Creates a csv file of the top similar results.
    html = df.to_html(index=False)
    return (html)
    
    #df_top_w_scores.to_csv("top_similar.csv", index=False)

def similarity_plot(input):
    df= similarity_score(input)
    fig, ax = plt.subplots()
    ax.scatter(df.similarity_score_title, df.similarity_score_description, s=300)
    ax.set_title("Similarity Score Distribution of Top 10 Similar Studies")
    ax.set(xlabel="Cosine Similarity Score based on Title", ylabel="Simillarity Score based on Study Description")
        
    return (fig)

#Test functions (temp)
def print_test(input):
    return (input + ": return from remote function")

