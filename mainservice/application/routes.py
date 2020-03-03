from flask import render_template, redirect, url_for, request, flash
from application import app
#from application.models import Superheroes, Users, Powers
from application.forms import Objectclass
import time
from requests import *
@app.route('/', methods=['GET','POST'])
@app.route('/home')
def home():
	objectclass=Objectclass()
	oc="x"
	no=get('http://sfia2_flask2_1:5000/no')
	site=get('http://sfia2_flask2_1:5000/site')
	container=get('http://sfia2_flask2_1:5000/container')
	locker=get('http://sfia2_flask2_1:5000/locker')

	if objectclass.validate_on_submit():
		if objectclass.objectclass.data.lower()=="safe":
			oc="Safe"
		if objectclass.objectclass.data.lower()=="euclid":
			oc="Euclid"
		if objectclass.objectclass.data.lower()=="keter":
			oc="Keter"
		if objectclass.objectclass.data.lower()=="test":
			oc="Thaumiel"
		return render_template("scp.html",oc=oc,no=no,site=site,container=container,locker=locker)

	return render_template("home.html", objectclass=objectclass)

#<form method='POST' action=''>
#  {{alterego.hidden_tag()}}
#  {{alterego.submit}}<br>
#</form>