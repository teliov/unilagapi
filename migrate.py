"""
Initial Migration
"""

import config
config.init()

from models import NewsItem

db = config.database_connection

db.create_table(NewsItem, True)