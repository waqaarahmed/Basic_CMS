
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Content

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    contents = Content.query.all()
    return render_template('index.html', contents=contents)


