from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
@app.route('/no')
def no():
	return str(randint(5000,10000))
@app.route('/site')
def site():
	return str(randint(1,200))
@app.route('/container')
def container():
	return str(randint(1,20))
#	if data=="safe":
#		return str(randint(1,200))
#	if data=="euclid":
#		return str(randint(1,20))
#	else:
#		return "0"
@app.route('/locker')
def locker():
	return str(randint(1,200))
@app.route('/redacted')
def redacted():
	return str(randint(1,100))