import config
# initialise settings here [application entry point]
config.init()

import json
import os
import math
from models import NewsItem
from bottle import request, Bottle, run, Response, response, abort
from playhouse.shortcuts import model_to_dict
from encoder import MyEncoder
from peewee import DoesNotExist


## Let's define an Auth middleware right here

class Auth(object):
	def __init__(self, app, api_key):
		self._app = app
		self._api_key = api_key

	def __call__(self, environ, start_response):
		try:
			header = environ.get('HTTP_UNILAG_API_KEY')
		except KeyError:
			header = None
		if header is not None and self._is_authenticated(header):
			return self._app(environ, start_response)
		else:
			response_headers = [("content-type", "application/json")]
			start_response("401 Authentication Failure", response_headers)
			error_object = {
				"error": "Authentication Error",
				"message": "This request has missing or invalid authentication"
			}
			return [json.dumps(error_object)]
			


	def _is_authenticated(self, header):
		return self._api_key == header

def get_pagination_object(query, page, limit):
	count = query.count()
	avg = count/limit
	rem = count%limit
	if avg == 0:
		num_pages = 1
	else:
		num_pages = avg + 1 if rem > 0 else avg

	next_page = page+1 if num_pages > page else None
	prev_page = page-1 if page > 1 else null
	return {
		"total": count,
		"num_of_pages": num_pages,
		"page": page,
		"next": next_page,
		"prev": prev_page
	}

unilagapi = Bottle()

@unilagapi.route('/items')
def get_items():
	page = int(request.query.page or 1)
	limit = int(request.query.limit or 100)
	items = NewsItem.select().paginate(page, limit)
	result = []
	for item in items:
		result.append(model_to_dict(item))

	pagination = get_pagination_object(NewsItem.select(), page, limit)
	response.set_header('content-type', 'application/json')
	response_obj = {
		"data": result,
		"pagination": pagination
	}
	return json.dumps(response_obj, cls=MyEncoder)

@unilagapi.route('/items/<news_id:int>')
def get_item(news_id):
	response.set_header("content-type", "application/json")
	try:
		item = NewsItem.select().where(NewsItem.id == news_id).get()
		obj = model_to_dict(item)
		response_obj = {
			"data": obj
		}
		return json.dumps(response_obj, cls=MyEncoder)
	except DoesNotExist:
		abort(404)

@unilagapi.error(code=404)
def error_404(error):
	response.set_header("content-type", "application/json")
	obj = {
		"error": "Route Not Found",
		"message": "This route does not exist"
	}
	return json.dumps(obj);

@unilagapi.error(code=500)
def error_500(error):
	response.set_header("content-type", "application/json")
	obj = {
		"error": "Server Error",
		"message": "Something went wrong on the server!"
	}
	return json.dumps(obj);


api_key = os.environ.get("API_KEY")
myapp = Auth(unilagapi, api_key)

run(myapp, host='localhost', port=5000)