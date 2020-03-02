from application import db, login_manager
from flask_login import UserMixin
class Powers(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	power = db.Column(db.String(30))

class Superheroes(db.Model):
	publisher = db.Column(db.String(30))
	name = db.Column(db.String(30))
	alterego = db.Column(db.String(30), primary_key=True)
	p1 = db.Column(db.Integer)
	p2 = db.Column(db.Integer)
	p3 = db.Column(db.Integer)
	team = db.Column(db.String(30))
	sidekick = db.Column(db.String(30))
	nemesis = db.Column(db.String(30))