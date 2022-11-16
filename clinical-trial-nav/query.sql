SELECT DISTINCT
conditions.nct_id,
brief_title,
conditions.name AS condition,
intervention_type,
interventions.name AS intervention
FROM conditions
LEFT JOIN interventions USING (nct_id) 
LEFT JOIN studies USING (nct_id)
WHERE conditions.name IN ('Type 2 Diabetes','Hypertension','Depression')
AND intervention_type != 'Other'