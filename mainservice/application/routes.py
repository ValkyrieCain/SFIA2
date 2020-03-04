from flask import render_template, redirect, url_for, request, flash
from application import app
#from application.models import
from application.forms import Objectclass
import time
from requests import *
@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
	objectclass=Objectclass()
	oc=""
	no=get('http://sfia2_flask2_1:5000/no')
	site=get('http://sfia2_flask2_1:5000/site')
	container=get('http://sfia2_flask2_1:5000/container')
	locker=get('http://sfia2_flask2_1:5000/locker')
	scp="SCP-"+str(no.text)
	if objectclass.validate_on_submit():
		if objectclass.objectclass.data.lower()=="safe":
			oc="Safe"
			#return render_template("safe.html",oc=oc,scp=scp,site=site,locker=locker)
		if objectclass.objectclass.data.lower()=="euclid":
			oc="Euclid"
			#return render_template("euclid.html",oc=oc,scp=scp,site=site,container=container)
		if objectclass.objectclass.data.lower()=="keter":
			oc="Keter"
			#return render_template("keter.html",oc=oc,scp=scp,site=site)
		if objectclass.objectclass.data.lower()=="test":
			oc="Thaumiel"
		return render_template("scp.html",oc=oc,scp=scp,site=site,container=container,locker=locker)

	return render_template("home.html", objectclass=objectclass)