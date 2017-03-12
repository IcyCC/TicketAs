from .apiTool import ApiTool
from ..app.models import *
import pypinyin

def initCity(db,tool = ApiTool()):
    cityList = tool.getCityList()
    for city in cityList:
        db.add(City(id=city.id, cityPinyin=city.city_pinyin, cinemaNum = city.count))
    db.commit()


def initCinema(db,tool = ApiTool()):
    cityList = City.query.all()
    for city in cityList:
        pages=tool.getCinemasByCity(city.id,page=1)['totalpage']
        for index in range(1,pages):
            cinemas = tool.getCinemasByCity(city.id, page=index)['data']
            for cinema in cinemas:
                db.add(Cinema(id=cinema.id, cinemaName=cinema.cinemaName,
                              address = cinema.address, telephone=cinema.telephone,
                              latitude=cinema.latitude, longitude=cinema.longitude, city=city))

    db.commit()


