SELECT DISTINCT
c.nct_id,
c.name AS condition,
t.intervention_type,
t.name AS intervention,
s.overall_status,
a.name AS country,
s.brief_title,
b.description AS study_description,
s.completion_date AS date
FROM conditions c
LEFT JOIN studies s USING (nct_id)
LEFT JOIN countries a USING (nct_id)
LEFT JOIN intervention_other_names i USING (nct_id)
LEFT JOIN interventions t USING (nct_id)
LEFT JOIN brief_summaries b USING (nct_id)
WHERE (a.name is not null)
AND (i.intervention_id is not null)
AND (t.name != 'Placebo')
AND (overall_status != 'Terminated')
AND (a.name IN ('United States'))
AND (s.completion_date > '2022-01-01' )
AND c.name IN ('Brain Tumors', 'Sarcoma', 'Breast Cancer', 'Leukemia', 'Pancreatic Cancer', 'Colorectal Cancer', 'Lymphoma', 'Head and Neck Cancer', 'Melanoma', 'Lung Cancer', 'Renal Cell Carcinoma', 'Multiple Myeloma', 'Esophageal Cancer', 'Adenocarcinoma', 'Ovarian Cancer' , 'Bladder Cancer', 'Liver Cancer')
