#coding=utf-8
from . import db,login_manager
from datetime import datetime,time
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from markdown import markdown
import bleach


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
            'cinemaName': self.cinemaName,
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
            'ticket_url': str(self.ticket_url),
            'movie': self.movie.tittle,
            'cinema': self.cinema.cinemaName
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

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(4),unique=True,index=True)
    password_hash=db.Column(db.String(128))
    role_id = db.Column(db.Integer)

    posts = db.relationship('Post', backref="user", lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('cant get password')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)

    def to_json(self):
        return {
            'id':str(self.id),
            'username':str(self.username) ,
            'role_id': str(self.role_id)
        }

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(300), index=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    body_html = db.Column(db.Text)
    abstract = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)

    def __repr__(self):
        return '<Post %r>' % self.tittle

    def to_json(self):
        return {
            'id': self.id,
            'tittle': self.tittle,
            'body': self.body,
            'timestamp':self.timestamp,
            'body_html':self.body_html,
            "abstract":self.abstract,
            "user":self.user.to_json()
        }

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                            'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                            'h1', 'h2', 'h3', 'p']
        target.body_html = bleach.linkify(bleach.clean(\
                markdown(value, output_format='html'),\
                tags=allowed_tags, strip=True))

    @staticmethod
    def on_changed_abstract(target, value, oldvalue, initiator):
        target.abstract = value[0:100]


db.event.listen(Post.body, 'set', Post.on_changed_body)
db.event.listen(Post.body, 'set', Post.on_changed_abstract)