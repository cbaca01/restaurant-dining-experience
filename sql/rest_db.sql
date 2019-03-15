DROP TABLE boros CASCADE;
CREATE TABLE boros (
	id 		INTEGER NOT NULL PRIMARY KEY,
	name  	VARCHAR(50) NOT NULL,

	UNIQUE (name)
);

DROP TABLE inspection_types CASCADE;
CREATE TABLE inspection_types (
	id 			INTEGER NOT NULL PRIMARY KEY,
	description text NOT NULL,

	UNIQUE (description)
);

DROP TABLE violation_codes CASCADE;
CREATE TABLE violation_codes (
	id 			INTEGER NOT NULL PRIMARY KEY,
	code 		VARCHAR(5) NOT NULL,
	description text NOT NULL,

	UNIQUE (code)
);

DROP TABLE critical_flags CASCADE;
CREATE TABLE critical_flags (
	id 			INTEGER NOT NULL PRIMARY KEY,
	description VARCHAR(50) NOT NULL,

	UNIQUE (description)
);

DROP TABLE cuisines CASCADE;
CREATE TABLE cuisines (
	id 			INTEGER NOT NULL PRIMARY KEY,
	description VARCHAR(150) NOT NULL,

	UNIQUE (description)
);

DROP TABLE actions CASCADE;
CREATE TABLE actions (
	id 			INTEGER NOT NULL PRIMARY KEY,
	description TEXT NOT NULL,

	UNIQUE (description)
);

DROP TABLE restaurants CASCADE;
CREATE TABLE restaurants (
	camis_id  	INTEGER NOT NULL PRIMARY KEY,
	dba 		VARCHAR (150) NOT NULL,
	boro_id		INTEGER REFERENCES boros(id) NOT NULL,
	building	VARCHAR(100),
	street		VARCHAR(200),
	zip_code	VARCHAR(5),
	phone		VARCHAR(15),
	cuisine_id	INTEGER REFERENCES cuisines(id) NOT NULL
);

DROP TABLE grades CASCADE;
CREATE TABLE grades (
	id 			INTEGER NOT NULL PRIMARY KEY,
	label		VARCHAR(20) NOT NULL,
	score		INTEGER NULL,

	UNIQUE (label)
);

DROP TABLE inspections CASCADE;
CREATE TABLE inspections (
	id  				SERIAL PRIMARY KEY,
	restaurant_id 		INTEGER REFERENCES restaurants(camis_id) NOT NULL,
	inspect_date		DATE NULL,
	action_id			INTEGER REFERENCES actions(id) NULL,
	violation_id		INTEGER REFERENCES violation_codes(id) NULL,
	critical_flag_id 	INTEGER REFERENCES critical_flags(id) NOT NULL,
	score				INTEGER NULL,
	grade_id			INTEGER REFERENCES grades(id) NULL,
	grade_date			DATE NULL,
	record_date			DATE NULL,
	inspect_type_id 	INTEGER REFERENCES inspection_types(id) NULL
);

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO rdxuser;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO rdxuser;