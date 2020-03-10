from application import db
class Scp(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	number = db.Column(db.Integer)
	site = db.Column(db.Integer)