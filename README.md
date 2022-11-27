<h3> WIP Readme for final projectg




<h3> #################################
# CSE6242-Project
Repo for our group to collaborate on the data and visual analytics final project

CONCERN: THE ICD-10 CM list of conditions doesn't seem like it will be a good first level for our visual. (JM)

## Class Resources
<a href="https://docs.google.com/document/d/e/2PACX-1vTL8p8euifAho6K6PSE_b63A1HTucl3GCyLJSvjGq7ySnncqTnFa8azPNoMpzG9Wx38p4jPzxaC3OZg/pub#h.z11rqsgxo2dh">Project Description</a> | <a href="https://poloclub.github.io/cse6242-2022fall-online/#schedule">Class Schedule</a>
<br>
<br>
<br>
## Project Docs
<a href="https://docs.google.com/document/d/1lqe5PRWkOnda88ej3mmXMtmSsfHRwsUhf-WpxVkttHg/edit?usp=sharing">Final Paper </a>
<br>
<a href="https://docs.google.com/document/d/1erX4OpgU211HFjJRcjamxAZiNvzC9xwRh5eIaOwE8Oc/edit?usp=sharing">Progress Report</a>
<br>
<a href="https://docs.google.com/document/d/1cjafBw1G33_HrOdqok-yhhjDRHoqFBKQ-x5F46Z5O3g/edit#">Weekly meeting notes</a>
<br>
<a href="https://docs.google.com/document/d/1ylCzLcUSYozW6nE28hbM9lZRbheKAYOK9GdyJh8Iz5A/edit?usp=sharing">Proposal</a>
<br>
<a href="https://www.youtube.com/watch?v=Q5EUbc9XGeM">Proposal Video</a>
<br>

## NLP Resources:
<a href="https://medium.com/analytics-vidhya/best-nlp-algorithms-to-get-document-similarity-a5559244b23b">Algorithms<a/>
<br>
<a href="https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html">TF-IDF Vectorizer (SKLearn)<a/>

## Data 
<b>Accessing <a href="https://clinicaltrials.gov/ct2/resources/download">ClinicalTrials.gov</a> through <a href="https://aact.ctti-clinicaltrials.org/">Clinical Trials Transformation Initiative</a> using pSQL</b>
<ul>
  <li>create an account on the clinical trials initiative page
  <li><a href="https://www.enterprisedb.com/downloads/postgres-postgresql-downloads">download pSQL</a>
  <li>set working directory to bin folder <i>C:\Program Files\PostgreSQL\15\bin</i>
  <li>run: <i> psql --host aact-db.ctti-clinicaltrials.org --port=5432 --username='example' --dbname=aact </i>
</ul>
<b> References </b>
<ul>
  <li><a href="https://aact.ctti-clinicaltrials.org/schema">Schema</a>
  <li><a href="https://aact.ctti-clinicaltrials.org/data_dictionary">Data Dictionary</a>
  <li>sample query: <i>select count(*) from studies;</i>
</ul>
<b>Resolving errors</b>
<ul>
  <li>if you're getting a UTF8 encoding error run the sql command <i>SET client_encoding TO 'UTF8';</i>
  <li>run \x to turn expanded display on/off to help with formatting
  <li> run \? for a list of additional commands
</ul>
<b>Connecting in Python</b>
<ul>
  <li>https://www.dataquest.io/blog/tutorial-connect-install-and-query-postgresql-in-python/
 </ul>
 <b>Connecting with PgAdmin</b>
  <ul>
  <li>https://aact.ctti-clinicaltrials.org/pgadmin
  </ul>
