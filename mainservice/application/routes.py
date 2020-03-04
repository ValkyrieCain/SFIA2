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
	no=get('http://sfia2_number_1:5000/no')
	site=get('http://sfia2_number_1:5000/site')
	container=get('http://sfia2_number_1:5000/container')
	locker=get('http://sfia2_number_1:5000/locker')
	scp="SCP-"+str(no.text)
	if objectclass.validate_on_submit():
		if objectclass.objectclass.data.lower()=="safe":
			oc="Safe"
			sadjective=get('http://sfia2_safe_1:5000/sadjective')
			snoun=get('http://sfia2_safe_1:5000/snoun')
			scategory=get('http://sfia2_safe_1:5000/scategory')
			sanomaly=get('http://sfia2_safe_1:5000/sanomaly')
			print(111)
			print(sadjective.text)
			#print(222)
			#print(sadjective.text[0])
			#print(333)
			#print(sadjective[1])
			#print(444)
			#print(sadjective[0])
			return render_template("safe.html",oc=oc,scp=scp,site=site,locker=locker,sadjective=sadjective,snoun=snoun,scategory=scategory,sanomaly=sanomaly)
		if objectclass.objectclass.data.lower()=="euclid":
			oc="Euclid"
			#eadjective=get('http://sfia2_euclid_1:5000/eadjective')
			#enoun=get('http://sfia2_euclid_1:5000/enoun')
			#ecategory=get('http://sfia2_safe_1:5000/ecategory')
			#eanomaly=get('http://sfia2_euclid_1:5000/eanomaly')
			#return render_template("euclid.html",oc=oc,scp=scp,site=site,container=container,eadjective=eadjective,enoun=enoun,ecategory=ecategory,eanomaly=eanomaly)
		if objectclass.objectclass.data.lower()=="keter":
			oc="Keter"
			#location=get('http://sfia2_keter_1:5000/location')
			#kadjective=get('http://sfia2_keter_1:5000/kadjective')
			#knoun=get('http://sfia2_keter_1:5000/knoun')
			#kcategory=get('http://sfia2_safe_1:5000/kcategory')
			#kanomaly=get('http://sfia2_keter_1:5000/kanomaly')
			#return render_template("keter.html",oc=oc,scp=scp,site=site,location=location,kadjective=kadjective,knoun=knoun,kcategory=kcategory,kanomaly=kanomaly)
		if objectclass.objectclass.data.lower()=="test":
			oc="Thaumiel"
		return render_template("scp.html",oc=oc,scp=scp,site=site,container=container,locker=locker,sadjective=sadjective)

	return render_template("home.html", objectclass=objectclass)