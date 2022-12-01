## Our Report
<a href="https://docs.google.com/document/d/1TU98gLuFX_0b1eKjLDSA7vy_Pt-TfzQrGJmKowTYLg0/edit?usp=sharing">Final Report</a>

## What data sources were used for this project?
The source of the data is from<a href="https://clinicaltrials.gov/ct2/resources/download"> ClinicalTrials.gov</a>. The entire dataset consists of 434,335 research studies in all 50 states and in 221 countries.
## Accessing the Data on Your Own
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
