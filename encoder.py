__author__ = 'teliov'
import json
import datetime
from time import mktime


class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        return json.JSONEncoder.default(self, obj)
