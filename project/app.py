from flask import Flask
from project.database import init_db
from project.models import __init__

# アプリケーションオブジェクトを作成する
def create_app():
	app = Flask(__name__)
	app.config.from_object('project.config.Config')

	# SQLAlchemyと連携させる
	init_db(app)

	return app

app = create_app()
from project.views import __init__
