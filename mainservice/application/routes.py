from flask import render_template, redirect, url_for, request, flash
from application import app, db
#from application.models import Superheroes, Users, Powers
from application.forms import Objectclass#, Hero, Search, Register, Login, Delete, Alterego, Alteregocreate, Dontdelete, Multidelete
import time
from requests import *
@app.route('/')
@app.route('/home')
def home():
	x=1
	response = get('http://numbergenerator_flask1:5000/no')
	print(response.text)
	if objectclass.validate_on_submit():
		x=1
		#return redirect(url_for('scp'))
	return render_template("home.html")
@app.route('/scp', methods=['GET','POST'])
def scp():
	return render_template("scp.html", objectclass=objectclass)

#<form method='POST' action=''>
#  {{alterego.hidden_tag()}}
#  {{alterego.submit}}<br>
#</form>
