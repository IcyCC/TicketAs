#coding=utf-8
import requests
from urllib import quote

class ApiTool:
    def __init__(self):
        pass

    def sendRequest(self,url,**kw):
        ## get orgin json file from api
        kw['key'] = '44000c9cfbd39f2c5a3499792d8eb673'
        r = requests.post(url=url, data=kw, verify=False)
        if r.json() is None:
            return None
        else:
            return r.json()

    def getCityList(self):
        return self.sendRequest(url="http://v.juhe.cn/movie/citys")["result"]

    def getCinemasByCity(self,cityid,page):
        return self.sendRequest(url="http://v.juhe.cn/movie/cinemas.search", cityid=cityid, page=page)["result"]

    def getTodayMovie(self,cityid):
        return self.sendRequest(url="http://v.juhe.cn/movie/movies.today",cityid = cityid)["result"]

    def getMovieById(self,movieid):
        return self.sendRequest(url="http://v.juhe.cn/movie/query",movieid = movieid)["result"]

    def getMovieByName(self,title):
        return self.sendRequest(url="http://v.juhe.cn/movie/query", tittle=title, smode =0)["result"]

    def getShowsByCinema(self,	cinemaid):
        return self.sendRequest(url="http://v.juhe.cn/movie/query", cinemaid=cinemaid, smode=0)["result"]



