from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # 追加

db = SQLAlchemy()

# connect by PyMySQL
'''
import pymysql.cursors
con = pymysql.connect(
	host='localhost',
	user='root',
	db='work_management',
	charset='utf8mb4',
	cursorclass=pymysql.cursors.DictCursor)
'''
# session
# https://qiita.com/ckern/items/a762b1bc0f192a55eae8
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
# mysqlのDBの設定
DATABASE = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (
	"root",
	"",
	"localhost",
	"template",
)
ENGINE = create_engine(
	DATABASE,
	encoding = "utf-8",
	echo=True # Trueだと実行のたびにSQLが出力される
)

# Sessionの作成
db_session = scoped_session(
# ORM実行時の設定。自動コミットするか、自動反映するなど。
 sessionmaker(
		autocommit = False,
		autoflush = False,
		bind = ENGINE
	)
)

def init_db(app):
	db.init_app(app)
	Migrate(app, db)  # 追加
