from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
import time
@app.route('/eadjective')
def eadjective():
	return sample(list/array/csv)
@app.route('/enoun')
def enoun():
	return randint(1,20)
@app.route('/eanomaly')
def eanomaly():
	return randint(1,200)