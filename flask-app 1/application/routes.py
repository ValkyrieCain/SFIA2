from flask import render_template, redirect, url_for, request, flash
#from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt, login_manager
#from application.models import Superheroes, Users, Powers
from application.forms import Objectclass#, Hero, Search, Register, Login, Delete, Alterego, Alteregocreate, Dontdelete, Multidelete
import time
@app.route('/')
@app.route('/home')
def home():
  if objectclass.validate_on_submit():
    return redirect(url_for('scp'))
  return render_template("home.html")
@app.route('/scp', methods=['GET','POST'])
def scp():
  return render_template("scp.html", objectclass=objectclass)

#<form method='POST' action=''>
#  {{alterego.hidden_tag()}}
#  {{alterego.submit}}<br>
#</form>