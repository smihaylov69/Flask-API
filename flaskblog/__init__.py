from flask import Flask, render_template,url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flaskblog.forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '479a33318c149edff83e99705e00d3f1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)