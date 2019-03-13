# our nyc_restaurants database schema

CREATE TABLE boros (
	id 		INTEGER NOT NULL PRIMARY KEY,
	name  	VARCHAR(50) NOT NULL,

	UNIQUE (id, name)
);

CREATE TABLE inspection_types (
	id 			INTEGER NOT NULL PRIMARY KEY,
	description VARCHAR(100) NOT NULL,

	UNIQUE (id, description)
);

CREATE TABLE violation_codes (
	id 			INTEGER NOT NULL PRIMARY KEY,
	code 		VARCHAR(5) NOT NULL,
	description text NOT NULL,

	UNIQUE (id, code)
);

CREATE TABLE critical_flags (
	id INTEGER NOT NULL PRIMARY KEY,
	name VARCHAR(10) NOT NULL,

	UNIQUE (id, name)
);

CREATE TABLE cuisines (
	id INTEGER NOT NULL PRIMARY KEY,
	description VARCHAR(10) NOT NULL,

	UNIQUE (id, description)
);

CREATE TABLE actions (
	id INTEGER NOT NULL PRIMARY KEY,
	description TEXT NOT NULL,

	UNIQUE (id, description)
);

CREATE TABLE violations (
	id 			INTEGER NOT NULL PRIMARY KEY,
	code  		VARCHAR(5) NOT NULL,
	description TEXT NOT NULL,

	UNIQUE (id, code, description)
);

CREATE TABLE dbas (
	id  		INTEGER NOT NULL PRIMARY KEY,
	dba 		VARCHAR (150) NOT NULL,
	boro_id		INTEGER REFERENCES boros(id) NOT NULL,
	building	VARCHAR(100),
	street		VARCHAR(200),
	zip_code	INTEGER,
	phone		INTEGER,
	cuisines_id	INTEGER REFERENCES cuisines(id) NOT NULL
);

CREATE TABLE critical_flags (
	id 			INTEGER NOT NULL,
	description	VARCHAR(50) NOT NULL,

	UNIQUE (id, description)
);

CREATE TABLE inspection_types (
	id  	INTEGER	NOT NULL PRIMARY KEY,
	name 	VARCHAR(250) NOT NULL,

	UNIQUE (id, name)
);

CREATE TABLE inspections (
	camis_id 			INTEGER PRIMARY KEY NOT NULL,
	dba_id INTEGER  	REFERENCES dbas(id) NOT NULL,
	inspection_date		DATE,
	action_id			INTEGER REFERENCES actions(id) NOT NULL,
	violation_id		INTEGER REFERENCES violations(id) NOT NULL,
	critical_flag_id 	INTEGER REFERENCES critical_flags(id) NOT NULL,
	score				INTEGER,
	grade				VARCHAR(10),
	grade_date			DATE,
	record_date			DATE,
	inspection_type_id 	INTEGER REFERENCES inspection_types(id) NOT NULL
);