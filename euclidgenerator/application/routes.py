from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
import time
@app.route('/eadjective')
def eadjective():
	adjective=["1.5 meter tall", "round", "carnivorous"]
	choice=sample(adjective,1)
	return choice[0]
@app.route('/enoun')
def enoun():
	noun=["a human of █████ descent", "███████", "a sentient bicycle", "a model train set"]
	choice=sample(noun,1)
	return choice[0]
@app.route('/ecategory')
def ecategory():
	category=["a weird", "a mad crazy"]
	choice=sample(category,1)
	return choice[0]
@app.route('/eanomaly')
def eanomaly():
	anomaly=["being fucked up", "███████"]
	choice=sample(anomaly,1)
	return choice[0]