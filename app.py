from flask import Flask, jsonify
from includes.database import *
app = Flask(__name__)

session = Session(engine)

@app.route("/getdata")
def getData():
	data = {}

	query = """
		SELECT r.camis_id AS camis,
			   r.dba,
			   b.name AS boro,
			   r.building,
			   r.street,
			   r.zip_code AS zipcode,
			   r.phone,
			   to_char(i.inspect_date, 'mm/dd/yyyy') AS inspection_date,
			   c.description AS cuisine_description,
			   a.description AS action,
			   v.code AS violation_code,
			   v.description AS violation_description,
			   cf.description AS critical_flag,
			   i.score,
			   g.label AS grade,
			   to_char(i.grade_date, 'mm/dd/yyyy') AS grade_date,
			   to_char(i.record_date, 'mm/dd/yyyy') AS record_date,
			   it.description AS inspection_type
		FROM inspections i
		INNER JOIN restaurants r ON i.restaurant_id = r.camis_id
		INNER JOIN boros b ON r.boro_id = b.id
		INNER JOIN cuisines c ON r.cuisine_id = c.id
		INNER JOIN actions a ON i.action_id = a.id
		INNER JOIN violation_codes v ON i.violation_id = v.id
		INNER JOIN critical_flags cf ON i.critical_flag_id = cf.id
		INNER JOIN grades g ON i.grade_id = g.id
		INNER JOIN inspection_types it ON i.inspect_type_id = it.id
		WHERE g.score >= :grade_score
	"""
	qParams = {'grade_score': 80}

	results = session.execute(query, qParams)

	data = []
	for i, row in enumerate(results):
		# This puts the data in dicionary format so it can outputed in JSON properly
		data.append(dict(zip(row.keys(), row)))

	return jsonify(data)
 
if __name__ == "__main__":
	app.run()





