from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
@app.route('/location')
def location():
	location=["Texas","England","Siberia","France","Maine","Germany","Italy","Morocco","Cuba","Antarctica","Sierra Lione","South Africa","Australia","[REDACTED]","█████████"]
	choice=sample(location,1)
	return choice[0]
@app.route('/kadjective')
def kadjective():
	adjective=["a 400 meter long", "a bright white"]
	choice=sample(adjective,1)
	return choice[0]
@app.route('/knoun')
def knoun():
	noun=["pond", "building built in 19██", "nuclear bomb", "train", "████████"]
	choice=sample(noun,1)
	return choice[0]
@app.route('/kcategory')
def kcategory():
	category=["a weird", "a mad crazy"]
	choice=sample(category,1)
	return choice[0]
@app.route('/kanomaly')
def kanomaly():
	anomaly=["being weird", "███████"]
	choice=sample(anomaly,1)
	return choice[0]