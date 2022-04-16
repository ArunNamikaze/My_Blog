from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    name = StringField("Name" , validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit =SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit =SubmitField("Log IN")

class CommentForm(FlaskForm):
    comment=CKEditorField("Post your comments", validators=[DataRequired()])
    submit = SubmitField("Comment")

class ContactForm(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    email=StringField("Email" ,validators=[DataRequired()])
    number=StringField("Phone Number", validators=[DataRequired()])
    message=StringField("Message" , validators=[DataRequired()])
    submit=SubmitField("Send")

