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
	noun=["pond", "building built in 19██", "nuclear bomb", "train", "████████","1940s era fighter plane",""]
	choice=sample(noun,1)
	return choice[0]
@app.route('/kcategory')
def kcategory():
	category=["a memetic","a ██████████","an antimemetic""an amorphous","an auditory","an autonomous","a biohazardous",
	"a cognitohazardous","a corrosive","an ectoentropic","an electrical","an empathetic","an extradimensional", "an extraterrestrial",
	"a foundation-made","a gaseous","a geological","a hallucinatory","a humanoid","a liquid",
	"a mechanical","a metamorphic","a microscopic","a mind-affecting","a neurological","an observational","an omnivorous","an organic",
	"an onotokinetic","a paradoxical","a parasitic","a photographic","a polyhedral","a predatory","a predictive","a radioactive","a reanimated",
	"a sapient","a self-repairing","a self-replicating","a sentient","a skeletal","a subterrenean","a telekinetic","a telepathic","a temporal",
	"a toxic","an uncontained","a vehicular"]
	choice=sample(category,1)
	return choice[0]
@app.route('/kanomaly')
def kanomaly():
	anomaly=["","","""" """]
	choice=sample(anomaly,1)
	return choice[0]