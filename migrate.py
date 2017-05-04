from yoyo import read_migrations, get_backend
from dotenv import load_dotenv
import os

curr_path = os.path.abspath(os.path.dirname(__file__))
dotenv_path = os.path.abspath(os.path.join(curr_path, '.env'))
migration_path = os.path.abspath(os.path.join(curr_path, 'migrations'))
load_dotenv(dotenv_path) 

environment = os.environ.get("ENVIRONMENT")

if environment == "development":
	database_conn_string = "sqlite:///%s/%s.db" %(curr_path, os.environ.get("DB_NAME"))
else:
	database_conn_string = "mysql://" + os.environ.get("DB_USER") + ":" + os.environ.get("DB_PASSWORD") + "@" + os.environ.get("DB_HOST") + "/" + os.environ.get("DB_NAME")


backend = get_backend(database_conn_string)
migrations = read_migrations(migration_path)
backend.apply_migrations(backend.to_apply(migrations))