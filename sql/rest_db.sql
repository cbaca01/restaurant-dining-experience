CREATE TABLE boros (
	id 		INTEGER NOT NULL PRIMARY KEY,
	name  	VARCHAR(50) NOT NULL,

	UNIQUE (id, name)
);

CREATE TABLE inspection_types (
	id 			INTEGER NOT NULL PRIMARY KEY,
	description text NOT NULL,

	UNIQUE (id, description)
);

CREATE TABLE violation_codes (
	id 			INTEGER NOT NULL PRIMARY KEY,
	code 		VARCHAR(5) NOT NULL,
	description text NOT NULL,

	UNIQUE (id, code)
);

CREATE TABLE critical_flags (
	id 			INTEGER NOT NULL PRIMARY KEY,
	description VARCHAR(50) NOT NULL,

	UNIQUE (id, description)
);

CREATE TABLE cuisines (
	id 			INTEGER NOT NULL PRIMARY KEY,
	description VARCHAR(150) NOT NULL,

	UNIQUE (id, description)
);

CREATE TABLE actions (
	id 			INTEGER NOT NULL PRIMARY KEY,
	description TEXT NOT NULL,

	UNIQUE (id, description)
);

CREATE TABLE restaurants (
	id  		INTEGER NOT NULL PRIMARY KEY,
	camis 		INTEGER NOT NULL,
	dba 		VARCHAR (150) NOT NULL,
	boro_id		INTEGER REFERENCES boros(id) NOT NULL,
	building	VARCHAR(100),
	street		VARCHAR(200),
	zip_code	VARCHAR(5),
	phone		VARCHAR(15),
	cuisine_id	INTEGER REFERENCES cuisines(id) NOT NULL,

	UNIQUE (id, camis, dba)
);

CREATE TABLE inspections (
	id  				SERIAL PRIMARY KEY,
	restaurant_id 		INTEGER REFERENCES restaurants(id) NOT NULL,
	inspect_date		DATE NULL,
	action_id			INTEGER REFERENCES actions(id) NOT NULL,
	violation_id		INTEGER REFERENCES violation_codes(id) NOT NULL,
	critical_flag_id 	INTEGER REFERENCES critical_flags(id) NOT NULL,
	score				INTEGER,
	grade				VARCHAR(10),
	grade_date			DATE NULL,
	record_date			DATE NULL,
	inspect_type_id 	INTEGER REFERENCES inspection_types(id) NOT NULL
);