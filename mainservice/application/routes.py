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
		if objectclass.objectclass.data.lower()=="test":
			oc="Thaumiel"
			occ=objectclass.objectclass.data.lower()
			return render_template("thaumiel.html",oc=oc,scp=scp,site=site,contain=(int(locker)/2))
		#elif objectclass.objectclass.data.lower()=="safe":
		elif int(no.text)%3==0:
			if int(redacted.text)==1:
				oc="Safe"
				return render_template("redacted.html",scp=scp,site=site,oc=oc)
			else:
				sadjective=get('http://sfia2_safe_1:5000/sadjective')
				adjective 	=sadjective.text
				snoun=get('http://sfia2_safe_1:5000/snoun')
				noun=snoun.text
				scategory=get('http://sfia2_safe_1:5000/scategory')
				category=scategory.text
				sanomaly=get('http://sfia2_safe_1:5000/sanomaly')
				anomaly=sanomaly.text
				return render_template("safe.html",scp=scp,site=site,adjective=adjective,noun=noun,category=category,anomaly=anomaly,locker=locker)
		#elif objectclass.objectclass.data.lower()=="euclid":
		elif int(no.text)%3==1:
			if int(redacted.text)==1:
				oc="Euclid"
				return render_template("redacted.html",scp=scp,site=site,oc=oc)
			else:
				eadjective=get('http://sfia2_euclid_1:5000/eadjective')
				adjective=eadjective.text
				enoun=get('http://sfia2_euclid_1:5000/enoun')
				noun=enoun.text
				ecategory=get('http://sfia2_euclid_1:5000/ecategory')
				category=ecategory.text
				eanomaly=get('http://sfia2_euclid_1:5000/eanomaly')
				anomaly=eanomaly.text
				return render_template("euclid.html",scp=scp,site=site,container=container,adjective=adjective,noun=noun,category=category,anomaly=anomaly)
		#elif objectclass.objectclass.data.lower()=="keter":
		elif int(no.text)%3==2:
			if int(redacted.text)==1:
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
	return render_template("home.html", objectclass=objectclass)