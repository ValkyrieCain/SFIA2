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
	no=get('http://sfia2_number_1:5000/no')
	scp="SCP-"+str(no.text)
	siteget=get('http://sfia2_number_1:5000/site')
	site=siteget.text
	containerget=get('http://sfia2_number_1:5000/container')
	container=containerget.text
	lockerget=get('http://sfia2_number_1:5000/locker')
	locker=lockerget.text
	redacted=get('http://sfia2_number_1:5000/redacted')
	if objectclass.validate_on_submit():
		if objectclass.objectclass.data.lower()=="safe":
			if str(redacted.text)=="1":
				oc="Safe"
				return render_template("redacted.html",scp=scp,site=site,oc=oc)
			else:
				sadjective=get('http://sfia2_safe_1:5000/sadjective')
				adjective=sadjective.text
				snoun=get('http://sfia2_safe_1:5000/snoun')
				noun=snoun.text
				scategory=get('http://sfia2_safe_1:5000/scategory')
				category=scategory.text
				sanomaly=get('http://sfia2_safe_1:5000/sanomaly')
				anomaly=sanomaly.text
				return render_template("safe.html",scp=scp,site=site,locker=locker,adjective=adjective,noun=noun,category=category,anomaly=anomaly)
		if objectclass.objectclass.data.lower()=="euclid":
			if str(redacted.text)=="1":
				oc="Euclid"
				return render_template("redacted.html",scp=scp,site=site,oc=oc)
			else:
				eadjective=get('http://sfia2_euclid_1:5000/eadjective')
				adjective=sadjective.text
				enoun=get('http://sfia2_euclid_1:5000/enoun')
				noun=snoun.text
				ecategory=get('http://sfia2_euclid_1:5000/ecategory')
				category=scategory.text
				eanomaly=get('http://sfia2_euclid_1:5000/eanomaly')
				anomaly=sanomaly.text
				return render_template("euclid.html",scp=scp,site=site,container=container,adjective=eadjective,noun=enoun,category=category,anomaly=anomaly)
		if objectclass.objectclass.data.lower()=="keter":
			if str(redacted.text)=="1":
				oc="Keter"
				return render_template("redacted.html",scp=scp,site=site,oc=oc)
			else:
				locationget=get('http://sfia2_keter_1:5000/location')
				location=locationget.text
				kadjective=get('http://sfia2_keter_1:5000/kadjective')
				adjective=kadjective.text
				knoun=get('http://sfia2_keter_1:5000/knoun')
				noun=knoun.text
				kcategory=get('http://sfia2_keter_1:5000/kcategory')
				category=kcategory.text
				kanomaly=get('http://sfia2_keter_1:5000/kanomaly')
				anomaly=kanomaly.text
				return render_template("keter.html",scp=scp,site=site,location=location,adjective=adjective,noun=noun,category=category,anomaly=anomaly)
		if objectclass.objectclass.data.lower()=="test":
			oc="Thaumiel"
			return render_template("scp.html",oc=oc,scp=scp,site=site,container=container,locker=locker)

	return render_template("home.html", objectclass=objectclass)