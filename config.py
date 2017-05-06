from dotenv import load_dotenv
from peewee import SqliteDatabase
import os

# initialise the database connection here
def init():
	global database_connection 
	global  curr_path 
	global  dotenv_path 
	global migration_path 
	global sqlite_db_path
	global has_loaded

	has_loaded = False
	dotenv_path = os.path.abspath(os.path.join(curr_path, '.env'))
	load_dotenv(dotenv_path)
	curr_path = os.path.abspath(os.path.dirname(__file__))
	migration_path = os.path.abspath(os.path.join(curr_path, 'migrations'))
	sqlite_db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.environ.get("DB_NAME")))

	

	environment = os.environ.get("ENVIRONMENT")
	if environment == "development":
		database_connection = SqliteDatabase(sqlite_db_path)
	else:
		database_connection = "find mysql database connection"

	has_loaded = True
