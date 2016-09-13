from wtforms import Form, StringField, validators, ValidationError

class WordCount(Form):
	count = StringField("Enter a sentence.", 
		validators=[validators.DataRequired()])