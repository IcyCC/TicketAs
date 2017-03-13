from .apiTool import ApiTool
from ..app.models import *
import pypinyin

def initCity(db,tool = ApiTool()):
    citys = tool.getCityList()
    for city in citys:
        db.add(City(id=city.id, cityPinyin=city.city_pinyin, cinemaNum = city.count))
    db.commit()


def initCinema(db,tool = ApiTool()):
    citys = City.query.all()
    for city in citys:
        pages=tool.getCinemasByCity(city.id,page=1)['totalpage']
        for index in range(1,pages):
            cinemas = tool.getCinemasByCity(city.id, page=index)['data']
            for cinema in cinemas:
                db.add(Cinema(id=cinema.id, cinemaName=cinema.cinemaName,
                              address = cinema.address, telephone=cinema.telephone,
                              latitude=cinema.latitude, longitude=cinema.longitude, city=city))

    db.commit()


def initMovie(db,tool=ApiTool()):
    citys = City.query.all()
    for city in citys:
        movies = tool.getTodayMovie(city.id)
        for movie in movies:
            movie = tool.getMovieById(movie.id)
            db.add(Movie(id=movie.id, tittle=movie.tittle,
                         pic_url=movie.poster, rating=movie.rating, detail=movie))
    db.commit()


def initShow(db,tool=ApiTool()):
    cinemas = Cinema.query.all()
    for cinema in cinemas:
        shows = tool.getShowsByCinema(cinema.id)['lists']
        for show in shows:
            movie = Movie.first_or_404(id=show.movieId)
            for broadcast in show['broadcast']:
                db.add(Show(time=in_time(broadcast.time), price=broadcast.price, ticket_url=broadcast.ticket_url,
                            hall=broadcast.hall, movie=movie, cinema=cinema))
    db.commit()

def intiDataBase(db,tool=ApiTool()):
    initCity(db=db, tool=tool)
    initCinema(db=db, tool=tool)
    initMovie(db=db, tool=tool)
    initShow(db=db, tool=tool)
