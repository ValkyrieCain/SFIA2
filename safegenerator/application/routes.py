from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
@app.route('/sadjective')
def sadjective():
	adjective=["a green", "a round", "a metallic", "a black", "a small", "a circular", "a white"]
	choice=sample(adjective,1)
	return choice[0]
@app.route('/snoun')
def snoun():
	noun=["rock", "spoon", "███████ brand handheld games console", "shelf", "bowl of rice"]
	choice=sample(noun,1)
	return choice[0]
@app.route('/scategory')
def scategory():
	category=["a weird", "a mad crazy"]
	choice=sample(category,1)
	return choice[0]
@app.route('/sanomaly')
def sanomaly():
	anomaly=["being fucked up", "███████"]
	choice=sample(anomaly,1)
	return choice[0]