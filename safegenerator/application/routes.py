from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
from requests import *
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
	category=["a memetic","a ██████████","an antimemetic""an amorphous","an auditory","an autonomous","a biohazardous",	"a carnivorous",
	"a cognitohazardous","a corrosive","a crystalline","an ectoentropic","an electrical","an empathetic","an extradimensional",	"an extraterrestrial",
	"a foundation-made","a gaseous","a geological","a hallucinatory","a humanoid","an indestructible","an intangible","a liquid"]
	choice=sample(category,1)
	return choice[0]
@app.route('/sanomaly')
def sanomaly():
	no=get('http://sfia2_number_1:5000/no')
	scp="SCP-"+str(no.text)
	siteget=get('http://sfia2_number_1:5000/site')
	site=siteget.text
	anomaly=["causing those who look at it to percieve it as a magnifying glass.","██████████ ███████ ████████ ████",
	"heating the air in a one meter radius around it to exactly twenty five degrees celcius", "creating a subspace bubble that absorbs all light",
	"causes seven Foundation terminals at Site "+site+" to display an image of "+scp+" at random intervals", "e", "f", "g"]
	choice=sample(anomaly,1)
	return choice[0]