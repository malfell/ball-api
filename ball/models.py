# import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# create database instance
db = SQLAlchemy()

# REPTILE MODEL
class Reptile(db.Model):
    __tablename__ = 'reptiles'

    # COLUMNS
    id = db.Column(db.Integer, primary_key = True)
    reptile = db.Column(db.String(250))
    info = db.Column(db.Text)