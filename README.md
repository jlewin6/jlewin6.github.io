# CSE6242-Project
Repo for our group to collaborate on the data and visual analytics final project

## Class Resources
<a href="https://docs.google.com/document/d/e/2PACX-1vTL8p8euifAho6K6PSE_b63A1HTucl3GCyLJSvjGq7ySnncqTnFa8azPNoMpzG9Wx38p4jPzxaC3OZg/pub#h.z11rqsgxo2dh">Project Description</a> | <a href="https://poloclub.github.io/cse6242-2022fall-online/#schedule">Class Schedule</a>
<br>
<br>
<br>
## Project Docs
<a href="https://docs.google.com/document/d/1cjafBw1G33_HrOdqok-yhhjDRHoqFBKQ-x5F46Z5O3g/edit#">Weekly meeting notes</a>
<br>
<a href="https://docs.google.com/document/d/1ylCzLcUSYozW6nE28hbM9lZRbheKAYOK9GdyJh8Iz5A/edit?usp=sharing">Proposal</a>
<br>
<a href="https://www.youtube.com/watch?v=Q5EUbc9XGeM">Proposal Video</a>
<br>
## Data 
Accessing <a href="https://clinicaltrials.gov/ct2/resources/download">ClinicalTrials.gov</a> data
<br>
<a href="https://www.enterprisedb.com/downloads/postgres-postgresql-downloads">download pSQL</a>
<br>
set working directory to bin folder
<br>
run: <i> psql --host aact-db.ctti-clinicaltrials.org --port=5432 --username='example' --dbname=aact </i>
<br>
sample query: <i>select count(*) from studies;</i>
<br>
<b><a href="https://aact.ctti-clinicaltrials.org/schema">Schema</a></b> 
resolving errors: if you're getting a UTF8 encoding error, run the sql command <i>SET client_encoding TO 'UTF8';</i>
<br>
run \x to turn on expanded display to help with formatting
