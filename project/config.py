import os

class DevelopmentConfig:
	# Flask
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(**{
		'user': os.getenv('DB_USER', 'root'),
		'password': os.getenv('DB_PASSWORD', ''),
		'host': os.getenv('DB_HOST', 'localhost'),
		'database': 'project',
	})

	# id/pw
	USERNAME = 'user'
	PASSWORD = 'pass'

	# session
	SECRET_KEY = 'nishihara'

	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_ECHO = False

Config = DevelopmentConfig
