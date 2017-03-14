#coding=utf-8
from . import db
from datetime import datetime,time


class City(db.Model):
    __tablename__ = 'citys'

    id = db.Column(db.Integer, index=True, primary_key=True)
    cityPinyin = db.Column(db.String(32), index=True)
    cinemaNum = db.Column(db.Integer)

    cinemas = db.relationship('Cinema', backref='city', lazy='dynamic')


class Cinema(db.Model):
    __tablename__ = 'cinemas'

    id = db.Column(db.Integer, index=True, primary_key=True)
    cinemaName = db.Column(db.String(128), index=True)
    address = db.Column(db.String(128))
    telephone = db.Column(db.String(32))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    city_id = db.Column(db.Integer, db.ForeignKey("citys.id"))
    shows = db.relationship('Show', backref='cinema', lazy="dynamic")


class Show(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, index=True, primary_key=True)
    time = db.Column(db.Time, index=True)
    price = db.Column(db.Integer)
    ticket_url = db.Column(db.String(64))
    hall = db.Column(db.String(32))

    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    cinema_id = db.Column(db.Integer, db.ForeignKey("cinemas.id"))

    @staticmethod
    def in_time(str):
        strs = str.split(':')
        nums = [int(s) for s in strs]
        return time(nums[0], nums[1])


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, index=True, primary_key=True)
    tittle = db.Column(db.String(64), index=True)
    pic_url = db.Column(db.String(64))
    rating = db.Column(db.Float)
    detail = db.Column(db.PickleType, index=True)
    shows = db.relationship('Show', backref='movie', lazy='dynamic')


