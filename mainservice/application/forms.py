from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError

class Objectclass(FlaskForm):
	objectclass=StringField(validators=[DataRequired(),Length(min=4,max=6)])
	submit=SubmitField('Generate SCP')
	def validate_objectclass(self, objectclass):
		if objectclass.data.lower()!="safe" and objectclass.data.lower()!="euclid" and objectclass.data.lower()!="keter" and objectclass.data.lower()!="test":
			raise ValidationError('Object Class incorrectly inputted. Please try again.')