# NYC Restaurants Grades

An API what allows you to check specific restaurants by cuisines and what letter grade.
This API was built using the following tools:
* [Python Flask](http://flask.pocoo.org/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [gunicorn](https://gunicorn.org/)

## Usage
Using any browser or any REST client type in the enter this url
```
https://intense-reaches-40403.herokuapp.com/getdata?grade='<GRADE>'&'cuisine_type='<CUISINE_TYPE>'
```
See below for details on the parameters

## Included files:
*NOTE*: Here are the core files for this project
* __includes/config.env__: enviornmental file that stores our database credentials to access our database.
* __sql/NYCAThaiFood.sql__: SQL file that has the SQL requirement for this assessment.
* __csv_etl.py__: ETL script that puts data from _DOHMH_New_York_City_Restaurant_Inspection_Results_ to our database.
* __app.py__: file that creates our REST calls
* __requirements.txt__: actual plugins and tools that are used.
* Procfile: file used to run our app on our webserver.

##Parameters
**GRADE**: the grade that we want see.	When this is entered we will see all the restaurants that are greater than or equal to this grade
**CUISINE_TYPE**: the cuisine type that we want to filter.	When this is entered we will see the restaurants that all have this cuisine type. 


##Output
```
*boro
*building
*camis
*dba
*grade
*phone
*street
*zipcode
```

## Errors
If a grade parameter is entered and it is not either A, B, or C, then this response will be outputed
```
[
	{
		"grade": "H is not a valid grade.  Only A, B, or C are acceptable"
	}
]
```
## Sample Output:
Click the links to view sample calls this API would do.
---
We are looking for restaurants that have at least a letter grade of B that serve Thai food.
<https://intense-reaches-40403.herokuapp.com/getdata?grade=B&cuisine_type=Thai>

We are looking for restaurants that have at least a letter grade of A that serve Mexican food
<https://intense-reaches-40403.herokuapp.com/getdata?grade=A&cuisine_type=mexican>

### Calls that would fail
We are looking for restaurants that have a letter grade of H that serve Greek food:
<https://intense-reaches-40403.herokuapp.com/getdata?grade=H&cuisine_type=Greek>