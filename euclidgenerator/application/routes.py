from flask import render_template, redirect, url_for, request, flash
from application import app
from random import *
@app.route('/eadjective')
def eadjective():
	adjective=["a 1.5 meter tall", "a round", "a carnivorous","an indestructible","an intangible"]
	choice=sample(adjective,1)
	return choice[0]
@app.route('/enoun')
def enoun():
	noun=["human of █████ descent", "███████", "sentient bicycle", "model train set","corporeal entity",""]
	choice=sample(noun,1)
	return choice[0]
@app.route('/ecategory')
def ecategory():
	category=["a memetic","a ██████████","an antimemetic""an amorphous","an auditory","an autonomous","a biohazardous",
	"a cognitohazardous","a corrosive","an ectoentropic","an electrical","an empathetic","an extradimensional", "an extraterrestrial",
	"a foundation-made","a gaseous","a geological","a hallucinatory","a humanoid","a liquid",
	"a mechanical","a metamorphic","a microscopic","a mind-affecting","a neurological","an observational","an omnivorous","an organic",
	"an onotokinetic","a paradoxical","a parasitic","a photographic","a polyhedral","a predatory","a predictive","a radioactive","a reanimated",
	"a sapient","a self-repairing","a self-replicating","a sentient","a skeletal","a subterrenean","a telekinetic","a telepathic","a temporal",
	"a toxic","an uncontained","a vehicular"]
	choice=sample(category,1)
	return choice[0]
@app.route('/eanomaly')
def eanomaly():
	anomaly=["being weird", "███████", "b", "c", "d", "e", "f", "g"]
	choice=sample(anomaly,1)
	return choice[0]