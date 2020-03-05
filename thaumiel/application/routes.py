from flask import Flask, render_template, redirect, url_for, request, flash, Response
from application import app
from random import *
@app.route('/thcontain', methods=['POST'])
def thcontain():
	if request.data.decode("utf-8")=="safe":
		return str(randint(1,100))
	elif request.data.decode("utf-8")=="euclid":
		return str(randint(1,20))
	elif request.data.decode("utf-8")=="keter":
		return str(randint(1,2))
	else:
		return "0"