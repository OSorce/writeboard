from flask.ext.wtf import Form
from wtforms import TextAreaField, SubmitField, HiddenField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError


class WritesForm(Form):
    key = HiddenField("Key")
    text = TextAreaField("Text", validators=[Required()])
    submit = SubmitField('Submit')
