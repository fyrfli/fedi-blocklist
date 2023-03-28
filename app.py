from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv, dotenv_values
from models import db, User
from datetime import date

load_dotenv()
env = dotenv_values()

app = Flask(__name__)

app.config['SECRET_KEY'] = env['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + env['DB_NAME']
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db.init_app(app)

with app.app_context():
    db.create_all()

the_year = date.today().year


@app.route('/')
def index():
    return render_template('index.html', the_year=the_year)
