SELECT DISTINCT
c.nct_id,
c.name AS condition,
t.intervention_type,
t.name AS intervention,
s.overall_status,
a.name AS country,
s.brief_title,
b.description AS study_description
FROM conditions c
LEFT JOIN studies s USING (nct_id)
LEFT JOIN countries a USING (nct_id)
LEFT JOIN intervention_other_names i USING (nct_id)
LEFT JOIN interventions t USING (nct_id)
LEFT JOIN brief_summaries b USING (nct_id)
WHERE a.name is not null AND i.intervention_id is not null AND intervention_type IN ('Drug') AND overall_status != 'Terminated' AND a.name IN ('United States')
AND c.name IN ('Brain Tumors', 'Sarcoma', 'Breast Cancer', 'Leukemia', 'Pancreatic Cancer', 'Colorectal Cancer', 'Lymphoma', 'Head and Neck Cancer', 'Melanoma', 'Lung Cancer', 'Renal Cell Carcinoma', 'Multiple Myeloma', 'Esophageal Cancer', 'Adenocarcinoma', 'Ovarian Cancer' , 'Bladder Cancer', 'Liver Cancer')
LIMIT 2000
