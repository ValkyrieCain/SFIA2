from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
import time
@app.route('/location')
def location():
	return sample(list/array/csv)
@app.route('/kadjective')
def kadjective():
	return randint(1,200)
@app.route('/knoun')
def knoun():
	return randint(1,20)
@app.route('/kanomaly')
def kanomaly():
	return randint(1,200)