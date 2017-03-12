#coding=utf-8
from . import db
from datetime import datetime


class City(db.Model):
    __tablename__ = 'citys'
    id = db.Column(db.Integer, index=True, primary_key=True)
    cityPinyin = db.Column(db.String(32), index=True)
    cinemaNum = db.Column(db.Integer)

    cinemas_id = db.Column(db.Integer, db.ForeignKey("cinema.id"))

class Cinema(db.Model):
    __tablename__ = 'cinemas'
    id = db.Column(db.Integer, index=True, primary_key=True)
    cinemaName = db.Column(db.String(128), index=True)
    address = db.Column(db.String(128))
    telephone = db.Column(db.String(32))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    city = db.relationship('City', backref='cinema', lazy='dynamic')
    shows_id = db.Column(db.Integer, db.ForeignKey("show.Id"))

class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, index=True, primary_key=True)
    time = db.Column(db.DateTime, index=True)
    price = db.Column(db.Integer)
    ticket_url = db.Column(db.String(64))
    movie = db.relationship('Movie', backerf='show', lazy='dynamic')

    cinema = db.relationship('Cinema', backref='show', lazy="dynamic")

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, index=True, primary_key=True)
    tittle = db.Column(db.String(64), index=True)
    rating = db.Column(db.Float)
    detail = db.Column(db.PickleType, index=True)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'))

