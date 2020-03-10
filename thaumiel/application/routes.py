from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
from requests import *
@app.route('/thaumiel')
def sanomaly():
	no=get('http://sfia2_main_1:5000/scp')
	scp=no.text
	siteget=get('http://sfia2_main_1:5000/site')
	site=siteget.text
	anomaly=["causing those who look at it to percieve it as a magnifying glass.","██████████ ███████ ████████ ████",
	"heating the air in a one meter radius around it to exactly twenty five degrees celcius", "creating a subspace bubble that absorbs all light",
	"causing seven Foundation terminals at "+site+" to display an image of "+scp+" at random intervals", "e", "f", "g"]
	choice=sample(anomaly,1)
	return choice[0]