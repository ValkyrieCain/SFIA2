from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
@app.route('/thcontain')
def thcontain(data):
	if data=="safe":
		return str(randint(1,100))
	elif data=="euclid":
		return str(randint(1,20))
	elif data=="keter":
		return str(randint(1,2))
	else:
		return "0"