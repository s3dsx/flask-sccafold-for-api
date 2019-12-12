from datetime import datetime, date, timedelta
from project.database import db

# for pw
import hashlib


class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), nullable=False)
	email = db.Column(db.String(64), nullable=False)
	password = db.Column(db.String(128), nullable=False)
	created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
