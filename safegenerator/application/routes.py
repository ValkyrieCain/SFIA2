from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
@app.route('/sadjective')
def sadjective():
	adjective=["a green","a round","a metallic","a black","a small","a circular","a white","a flat","a spherical","a translucent"]
	choice=sample(adjective,1)
	return choice[0]
@app.route('/snoun')
def snoun():
	noun=["rock", "spoon", "███████ brand handheld games console", "shelf", "bowl of rice"]
	choice=sample(noun,1)
	return choice[0]
@app.route('/scategory')
def scategory():
	category=["a memetic","a ██████████","an antimemetic""an amorphous","an auditory","an autonomous","a biohazardous","a carnivorous","a cognitohazardous","a corrosive","a crystalline","an ectoentropic", "an electrical"]
	choice=sample(category,1)
	return choice[0]
@app.route('/sanomaly')
def sanomaly():
	anomaly=["causing those who look at it to percieve it as a magnifying glass."
	,"██████████ ███████ ████████ ████","heating the air in a one meter radius around it to exactly twenty five degrees celcius",
	"c", "d", "e", "f", "g"]
	choice=sample(anomaly,1)
	return choice[0]