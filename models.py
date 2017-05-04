from peewee import PrimaryKeyField, CharField, DateTimeField, TextField, Model
import config

try:
	has_loaded_config = config.has_loaded
except AttributeError:
	has_loaded_config = False

if not has_loaded_config:
	config.init()


class BaseModel(Model):
	class Meta:
		database = config.database_connection

class NewsItem(BaseModel):
	id = PrimaryKeyField()
	news_hash = CharField(unique=True)
	slug = CharField(unique=True)
	news_title = CharField()
	news_link =  CharField()
	date_updated = DateTimeField()
	intro_text = TextField()
	scrapped_at =DateTimeField()

	class Meta:
		order_by = ['-scrapped_at']
		db_table = 'news_items'