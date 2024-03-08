from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired



class PostForm(FlaskForm):
    post_title = TextAreaField("Title", validators=[DataRequired()])