#coding=utf-8
from . import db
from datetime import datetime,time


class City(db.Model):
    __tablename__ = 'citys'

    id = db.Column(db.Integer, index=True, primary_key=True)
    cityPinyin = db.Column(db.String(32), index=True)
    cinemaNum = db.Column(db.Integer)

    cinemas = db.relationship('Cinema', backref='city', lazy='dynamic')

    def to_json(self):
        return {
            'id': str(self.id),
            'cityPinyin': self.cityPinyin,
            'cinemaNum':str(self.cinemaNum)
        }


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

    def to_json(self):
        return {
            'id': str(self.id),
            'cinemaName': self.cityPinyin,
            'address': self.address,
            'telephone': self.telephone,
            'latitude':str(self.latitude),
            'longitude':str(self.longitude),
            'city_id':str(self.city_id)
        }


class Show(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, index=True, primary_key=True)
    time = db.Column(db.Time, index=True)
    price = db.Column(db.Integer)
    ticket_url = db.Column(db.String(64))
    hall = db.Column(db.String(32))

    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    cinema_id = db.Column(db.Integer, db.ForeignKey("cinemas.id"))

    def to_json(self):
        return {
            'id': str(self.id),
            'time': str(self.time),
            'price': str(self.price),
            'ticket_url': self.ticket_url,
            'movie_id':str(self.movie_id),
            'cinema_id':str(self.cinema_id)
        }

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

    def to_json(self):
        return {
            'id': str(self.id),
            'tittle': self.tittle,
            'pic_url': self.pic_url,
            'rating': str(self.rating),
            'detail':self.detail
        }