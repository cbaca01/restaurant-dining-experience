from includes.database import *
import datetime
import csv

# create buffer
def get_table_dict(table, column_key, column_id='id'):
	data = {}

	results = session.query(table).all()
	for u in results:
		ckey = getattr(u, column_key)
		cid = getattr(u, column_id)
		data[ckey] = cid

	return data


# insert into table and when done return the ID from the list_buffer
def insert_into_table(table, params, list_bfr, key_val, id_col='id'):
	# if Value is empty, return
	if len(key_val.strip()) == 0:
		return params[id_col]

	row_id = None
	if key_val not in list_bfr:
		ins = table(**params)

		session.add(ins)
		session.flush()
		row_id = getattr(ins, id_col) 
		session.commit()

		list_bfr[key_val] = row_id
	else:
		row_id = list_bfr[key_val]

	return row_id

# convert date to database date
def convert_date(date_str):
	return null() if date_str=='' else datetime.datetime.strptime(date_str, '%m/%d/%Y').date()

# set column to null if null
def set_to_null(input_str, id_col=None):
	if id_col != None:
		return null() if (len(input_str)==0) else id_col
	else:
		return null() if (len(input_str)==0) else input_str


session = Session(engine)
dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
with open('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', 'r') as f:
	reader = csv.reader(f)

	# input buffers
	boros_bfr = get_table_dict(boros, column_key='name')
	cuisines_bfr = get_table_dict(cuisines, column_key='description')
	actions_bfr = get_table_dict(actions, column_key='description')
	violation_codes_bfr = get_table_dict(violation_codes, column_key='code')
	inspection_types_bfr = get_table_dict(inspection_types, column_key='description')
	critical_flags_bfr = get_table_dict(critical_flags, column_key='description')
	restaurants_bfr = get_table_dict(restaurants, column_key='camis_id', column_id='camis_id')

	# creating the grades table
	grades_bfr = get_table_dict(grades, column_key='label')

	next(reader)
	for row in reader:
		# Insert into boros
		boro = row[2].strip()
		params = {'id': (len(boros_bfr)+1), 'name': boro}
		boro_id = insert_into_table(boros, params, boros_bfr, key_val=boro)

		# Insert into cuisines
		cuisine = row[7].strip()
		params = {'id': (len(cuisines_bfr)+1), 'description': cuisine}
		cuisine_id = insert_into_table(cuisines, params, cuisines_bfr, key_val=cuisine)

		# Insert into actions
		action = row[9].strip()
		params = {'id': (len(actions_bfr)+1), 'description': action}
		action_id = insert_into_table(actions, params, actions_bfr, key_val=action)

		# Insert into violation_codes
		violation_code = row[10]
		violation_description = row[11]
		params = {'id': (len(violation_codes_bfr)+1), 'code': violation_code, 'description': violation_description}
		violation_code_id = insert_into_table(violation_codes, params, violation_codes_bfr, key_val=violation_code)

		# Insert into inspection_types
		inspection_type = row[17]
		params = {'id': (len(inspection_types_bfr)+1), 'description': inspection_type}
		inspection_type_id = insert_into_table(inspection_types, params, inspection_types_bfr, key_val=inspection_type)

		# Insert into critical_flags
		critical_flag = row[12]
		params = {'id': (len(critical_flags_bfr)+1), 'description': critical_flag}
		critical_flag_id = insert_into_table(critical_flags, params, critical_flags_bfr, key_val=critical_flag)

		# Insert into grades
		grade = row[14]
		params = {'id': (len(grades_bfr)+1), 'label': grade}
		if grade=='A':
			params['score'] = 100
		elif grade=='B':
			params['score'] = 80
		elif grade=='C':
			params['score'] = 70

		grade_id = insert_into_table(grades, params, grades_bfr, key_val=grade)

		# Insert our restaurants table
		camis_id = row[0]
		params = {
			'camis_id' 	 : camis_id,
			'dba'		 : row[1],
			'boro_id'	 : boro_id,
			'building'   : row[3],
			'street'     : row[4],
			'zip_code'   : row[5],
			'phone'	     : row[6],
			'cuisine_id' : cuisine_id
		}
		restaurant_id = insert_into_table(restaurants, params, restaurants_bfr, key_val=camis_id, id_col='camis_id')

		# # insert into inspections
		# # this is done "manually" due to every record being unique
		params = {
			'restaurant_id' 	 : restaurant_id,
			'inspect_date'    	 : convert_date(row[8]),
			'action_id'		     : set_to_null(action, action_id),
			'violation_id'	     : set_to_null(violation_code, violation_code_id),
			'critical_flag_id'   : critical_flag_id,
			'score'			     : set_to_null(row[13]),
			'grade_id'			 : set_to_null(grade, grade_id),
			'grade_date'	     : convert_date(row[15]),
			'record_date'		 : convert_date(row[16]),
			'inspect_type_id'	 : set_to_null(inspection_type, inspection_type_id)
		}
		ins = inspections(**params)

		session.add(ins)
		session.flush() 
		session.commit()

	
	del	boros_bfr
	del cuisines_bfr
	del actions_bfr
	del violation_codes_bfr
	del inspection_types_bfr
	del critical_flags_bfr
	del restaurants_bfr