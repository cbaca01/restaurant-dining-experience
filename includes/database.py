import os
from os.path import join, dirname
from dotenv import load_dotenv

from sqlalchemy import create_engine, select, MetaData, Table, null
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.automap import automap_base

# Loading config.env file to get our data
dotenv_path = join(dirname(__file__), 'config.env')
load_dotenv(dotenv_path)

# retrieving our database connection parameters
DBHOST = os.getenv('DBHOST')
DBNAME = os.getenv('DBNAME')
DBUSER  = os.getenv('DBUSER')
DBPASSWORD = os.getenv('DBPASSWORD')

Base = automap_base()

engine = create_engine('postgresql://' + DBUSER + ':' + DBPASSWORD + '@' + DBHOST + '/' + DBNAME)
connection = engine.connect()

metadata = MetaData(bind=None)

# Reflect tables
Base.prepare(engine, reflect=True)

# Tables we use as List Tables
boros = Base.classes.boros
cuisines = Base.classes.cuisines
actions = Base.classes.actions
violation_codes = Base.classes.violation_codes
inspection_types = Base.classes.inspection_types
critical_flags = Base.classes.critical_flags
grades = Base.classes.grades

# Junction Tables
restaurants = Base.classes.restaurants

# Main table
inspections = Base.classes.inspections
