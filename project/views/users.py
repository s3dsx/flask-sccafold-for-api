from flask import request, redirect, url_for, render_template, flash, session
from project.app import app
from project.database import db
from project.models import __init__
from project.models.users import *

@app.route('/user')
def show_users():
	return 200
