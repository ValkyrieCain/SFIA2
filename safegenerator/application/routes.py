from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
import time
@app.route('/sadjective')
def sadjective():
	return sample(list/array/csv)
@app.route('/snoun')
def snoun():
	return str(randint(1,20))
@app.route('/sanomaly')
def sanomaly():
	return randint(1,200)