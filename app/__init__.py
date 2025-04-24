from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import views

app = Flask(__name__)  

app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)