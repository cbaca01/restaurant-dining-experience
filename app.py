from flask import Flask, request, url_for, jsonify
from includes.database import *
app = Flask(__name__)

session = Session(engine)

# Request for getting our data
@app.route("/getdata", methods=['GET'])
def getData():
	grade = request.args.get('grade')
	cuisine_type = request.args.get('cuisine_type')

	# Query that retrieves call
	query = """
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
			SELECT c.id FROM cuisines c WHERE LOWER(c.description) = LOWER(:cuisine_type)
		)
		GROUP BY r.camis_id, r.dba, b.name, g.label, g.score
		HAVING g.score >= (
			SELECT g.score FROM grades g WHERE LOWER(g.label) = LOWER(:grade)
		)
		ORDER BY r.dba
	"""

	qParams = {
		'grade': grade,
		'cuisine_type': cuisine_type
	}
	results = session.execute(query, qParams)

	data = []
	for i, row in enumerate(results):
		# This puts the data in dicionary format so it can outputed in JSON properly
		data.append(dict(zip(row.keys(), row)))

	return jsonify(data)
 
if __name__ == "__main__":
	app.run()





