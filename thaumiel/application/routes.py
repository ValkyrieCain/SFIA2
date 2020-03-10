from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
from requests import *
@app.route('/thaumiel')
def thaumiel():
	no=get('http://sfia2_main_1:5000/scp')
	scp=no.text
	siteget=get('http://sfia2_main_1:5000/site')
	site=siteget.text
	anomaly="causes seven Foundation terminals at "+site+" to display an image of "+scp+" at random intervals"
	return anomaly