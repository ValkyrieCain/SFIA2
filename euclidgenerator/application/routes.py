from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
@app.route('/eadjective')
def eadjective():
	adjective=["a 1.5 meter tall", "a round", "a carnivorous"]
	choice=sample(adjective,1)
	return choice[0]
@app.route('/enoun')
def enoun():
	noun=["human of █████ descent", "███████", "sentient bicycle", "model train set"]
	choice=sample(noun,1)
	return choice[0]
@app.route('/ecategory')
def ecategory():
	category=["a weird", "a mad crazy"]
	choice=sample(category,1)
	return choice[0]
@app.route('/eanomaly')
def eanomaly():
	anomaly=["being weird", "███████"]
	choice=sample(anomaly,1)
	return choice[0]