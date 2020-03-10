from application import db
class Scp(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	number = db.Column(db.Integer)
	site = db.Column(db.Integer)
	def __repr__(self):
		return ''.join(['Number: ', self.number, '\r\n',
			'Site: ', self.site, '\r\n'])