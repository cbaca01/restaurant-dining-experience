SELECT r.camis_id AS camis,
	   r.dba,
	   b.name AS boro,
	   r.building,
   	   r.street,
	   r.zip_code AS zipcode,
	   r.phone,
	   g.label AS grade
FROM inspections i
INNER JOIN restaurants r ON i.restaurant_id = r.camis_id
INNER JOIN boros b ON r.boro_id = b.id
INNER JOIN cuisines c ON r.cuisine_id = c.id
INNER JOIN actions a ON i.action_id = a.id
INNER JOIN violation_codes v ON i.violation_id = v.id
INNER JOIN critical_flags cf ON i.critical_flag_id = cf.id
INNER JOIN grades g ON i.grade_id = g.id
INNER JOIN inspection_types it ON i.inspect_type_id = it.id
WHERE c.id = (
	SELECT c.id FROM cuisines c WHERE LOWER(c.description) = LOWER('Thai')
)
GROUP BY r.camis_id, r.dba, b.name, g.label, g.score
HAVING g.score >= (
	SELECT g.score FROM grades g WHERE LOWER(g.label) = LOWER('A')
)
ORDER BY r.dba;