from flask_wtf import Form
from wtforms import StringField, TextAreaField, HiddenField
from wtforms.validators import DataRequired


class CreateForm(Form):
    post_id = HiddenField()
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])


class CommentForm(Form):
    author = StringField('Author', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    post_id = HiddenField(validators=[DataRequired()])
