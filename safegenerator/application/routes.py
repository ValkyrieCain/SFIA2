from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
from requests import *
@app.route('/sadjective')
def sadjective():
	adjective=["a green","a round","a metallic","a black","a small","a circular","a minature","a white","a flat","a spherical","a translucent","a wooden",
	"a crystalline","a magnetic"]
	choice=sample(adjective,1)
	return choice[0]
@app.route('/snoun')
def snoun():
	noun=["rock", "spoon", "███████ brand handheld games console", "shelf", "bowl of rice","cheese grater","piece of tofu",""]
	choice=sample(noun,1)
	return choice[0]
@app.route('/scategory')
def scategory():
	category=["a memetic","a ██████████","an antimemetic""an amorphous","an auditory","an autonomous","a biohazardous","a carnivorous",
	"a cognitohazardous","a corrosive","an ectoentropic","an electrical","an empathetic","an extradimensional", "an extraterrestrial",
	"a foundation-made","a gaseous","a geological","a hallucinatory","a humanoid","an indestructible","an intangible","a liquid",
	"a mechanical","a metamorphic","a microscopic","a mind-affecting","a neurological","an observational","an omnivorous","an organic",
	"an onotokinetic","a paradoxical","a parasitic","a photographic","a polyhedral","a predatory","a predictive","a radioactive","a reanimated",
	"a sapient","a self-repairing","a self-replicating","a sentient","a skeletal","a subterrenean","a telekinetic","a telepathic","a temporal",
	"a toxic","an uncontained","a vehicular"]
	choice=sample(category,1)
	return choice[0]
@app.route('/sanomaly')
def sanomaly():
	no=get('http://sfia2_main_1:5000/scp')
	scp=no.text
	siteget=get('http://sfia2_main_1:5000/site')
	site=siteget.text
	anomaly=["causing those who look at it to percieve it as a magnifying glass.","██████████ ███████ ████████ ████",
	"heating the air in a one meter radius around it to exactly twenty five degrees celcius", "creating a subspace bubble that absorbs all light",
	"causes seven Foundation terminals at "+site+" to display an image of "+scp+" at random intervals","turning all food that touches it into bars of 9█.███% pure gold"]
	choice=sample(anomaly,1)
	return choice[0]