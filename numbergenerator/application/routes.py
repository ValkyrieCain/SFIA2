from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
import time
@app.route('/no')
def no():
	return str(randint(1,10000))
@app.route('/site')
def site():
	return str(randint(1,200))
@app.route('/container')
def container():
	return str(randint(1,20))
@app.route('/locker')
def locker():
	return str(randint(1,200))
@app.route('/redacted')
def redacted():
	return str(randint(1,150))