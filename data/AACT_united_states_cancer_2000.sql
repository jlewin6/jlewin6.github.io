SELECT DISTINCT
c.nct_id, 
c.name AS name_condition,
s.brief_title, s.overall_status,
a.name AS name_country,
string_agg(i.intervention_id::character varying, ' / ') AS id_intervention,
string_agg(i.name, ' / ') AS name_intervention, 
t.intervention_type, 
b.description AS study_description

FROM conditions c
LEFT JOIN studies s USING (nct_id)
LEFT JOIN countries a USING (nct_id)
LEFT JOIN intervention_other_names i USING (nct_id)
LEFT JOIN interventions t USING (nct_id) 
LEFT JOIN brief_summaries b USING (nct_id)
WHERE a.name is not null AND i.intervention_id is not null AND intervention_type IN ('Drug') AND overall_status != 'Terminated' AND a.name IN ('United States')
AND c.name IN ('Brain Tumors', 'Sarcoma', 'Breast Cancer', 'Leukemia', 'Pancreatic Cancer', 'Colorectal Cancer', 'Lymphoma', 'Head and Neck Cancer', 'Melanoma', 'Lung Cancer', 'Renal Cell Carcinoma', 'Multiple Myeloma', 'Esophageal Cancer', 'Adenocarcinoma', 'Ovarian Cancer' , 'Bladder Cancer', 'Liver Cancer')

GROUP BY c.nct_id, c.name, s.brief_title, s.overall_status, a.name, t.intervention_type, b.description

LIMIT 2000
