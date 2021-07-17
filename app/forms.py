from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    search = StringField("", validators = [DataRequired()], render_kw={"placeholder": "Tell us a song stuck in your head <3"})
    submit = SubmitField("Search for similar songs")