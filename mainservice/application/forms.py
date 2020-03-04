from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField#,IntegerField,PasswordField,BooleanField,FormField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError
#from application.models import Users, Superheroes

class Objectclass(FlaskForm):
	objectclass=StringField(validators=[DataRequired(),Length(min=4,max=6)])
	submit=SubmitField('Generate SCP')
	def validate_class(self, objectclass):
		if objectclass.objectclass.data.lower()=="work":
			raise ValidationError('Object Class incorrectly inputted. Please try again.')
		#if objectclass.objectclass.data.lower()!="safe" and objectclass.objectclass.data.lower()!="euclid" and objectclass.objectclass.data.lower()!="keter" and objectclass.objectclass.data.lower()!="test":
		#	raise ValidationError('Object Class incorrectly inputted. Please try again.')