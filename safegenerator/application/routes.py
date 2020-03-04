from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
import time
@app.route('/sadjective')
def sadjective():
	adjective=["a green", "a round", "a metallic", "a black", "a small", "a circular", "a white"]
	return sample(adjective,1)
@app.route('/snoun')
def snoun():
	return str(randint(1,20))
@app.route('/sanomaly')
def sanomaly():
	return randint(1,200)