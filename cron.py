#! /usr/bin/env python

## To be Run every hour

from scrap import UnilagScrap as Scrap
from models import NewsItem
from datetime import datetime

scrapper = Scrap()

news_items = scrapper.get_news_items()

for item in news_items:
	## let's insert stuff
	# first check that it does not already exist!
	to_db = NewsItem.select().where(NewsItem.slug == item['slug'])
	if len(to_db) == 0:
		# item has not been in the db before
		to_db = NewsItem(news_hash=item['news_hash'], slug=item['slug'], news_title=item['title'],
			news_link=item['link'], date_updated=item['date_updated'], intro_text=item['intro_text'], scrapped_at=datetime.now())
		to_db.save()
	else:
		to_db = to_db.get()
		# check if the hash has changed
		if to_db.news_hash != item['news_hash']:
			to_db.news_hash = item['news_hash']
			to_db.news_title = item['news_title']
			to_db.news_link = item['link']
			to_db.date_updated = item['date_updated']
			to_db.intro_text = item['intro_text']
			to_db.save()