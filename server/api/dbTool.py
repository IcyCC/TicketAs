from .apiTool import *
from app.models import *

def initCity(db, tool=ApiTool()):
    citys = tool.getCityList()
    for city in citys:
        c = City(id=int(city.get('id')), cityPinyin=city.get('city_pinyin'), cinemaNum=int(city.get('count')))
        db.session.add(c)
    db.session.commit()


def initCinema(db, tool=ApiTool()):
    #citys = City.query.all()
    citys = City.query.filter_by(id=2).all()
    for city in citys:
        pages = tool.getCinemasByCity(city.id, page=1)['totalpage']
        for index in range(1,pages+1):
            cinemas = tool.getCinemasByCity(city.id, page=index)['data']
            for cinema in cinemas:
                print cinema
                db.session.add(Cinema(id=cinema.get('id'), cinemaName=cinema.get('cinemaName'),
                                      address=cinema.get('address'), telephone=cinema.get('telephone'),
                                      latitude=cinema.get('latitude'), longitude=cinema.get('longitude'),
                                      city_id=city.id))
    db.session.commit()


def initMovie(db, tool=ApiTool()):
    #citys = City.query.all()
    citys = City.query.filter_by(id=1).all()
    for city in citys:
        movies = tool.getTodayMovie(city.id)
        for movie in movies:
            print movie
            m = tool.getMovieById(movie.get('movieId'))
            if m is not None:
                db.session.add(Movie(id=m.get('movieId'), tittle=m.get('tittle'),
                                     pic_url=m.get('poster'), rating=m.get('rating_count'), detail=m))
            else:
                db.session.add(Movie(id=movie.get('movieId'), tittle=movie.get('movieName'),
                                     pic_url=movie.get('pic_url')))
        db.session.commit()


def initShow(db, tool=ApiTool()):
    cinemas = Cinema.query.all()
    for cinema in cinemas:
        print cinema.id
        shows = tool.getShowsByCinema(cinema.id)['lists']
        if shows is not None:
            print shows
            for show in shows:
                print show
                movie = Movie.query.filter_by(id=show.get("movieId")).first_or_404()
                for broadcast in show['broadcast']:
                    db.session.add(Show(time=Show.in_time(broadcast.get('time')), price=broadcast.get('price'),
                                        ticket_url=broadcast.get('ticket_url'), hall=broadcast.get('hall'),
                                        movie=movie, cinema=cinema))
            db.session.commit()


