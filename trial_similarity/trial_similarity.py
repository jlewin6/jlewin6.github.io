import json
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity

# We need to provide a datafram with trial ID's and descriptions
# ...this is an example with all of the trials that had "stroke" as the condition
df = pd.read_csv("stroke_desc.csv")

# This gives the index of the study that we want to compare the other studies to.
selected_index = 10
top_n = 5

# Descriptions turned into a list
desc_collection = list(df['description'])

# Creates a vectorizer that will convert descriptions into vectors using idf removing stop words
vectorizer = TfidfVectorizer(stop_words = text.ENGLISH_STOP_WORDS, use_idf=True)
X = vectorizer.fit_transform(desc_collection)

# Finds the cosine similarity between the
A = cosine_similarity(X[selected_index], X)

# Creates a df of the top n similarity scores
# Since A is a nested array, we need to use the A[0] to get within it.
# The last record is the selected record and isn't included
df_sim_score = pd.DataFrame({'similarity_score': np.sort(A[0])[-(top_n+1):-1]})

# Creates a df of the clinical trial records with  the top n similarity scores to
# the 'selected' trial. The last record is the selected record and isn't included
df_top_trials = df.iloc[(np.argsort(A[0]))[-(top_n+1):-1], :].reset_index(drop=True)

# Concatenates the list of trials with the corresponding similiarity scores.
df_top_w_scores = pd.concat([df_top_trials, df_sim_score], axis=1)

# Creates a csv file of the top similar results.
df_top_w_scores.to_csv("top_similar.csv", index=False)

