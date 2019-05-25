# -*- coding: utf-8 -*-
import scrapy
import re
from graduation.items import FilmDetailItem
import pymongo
from graduation.settings import MONGO_URI,MONGO_DB
import http.cookiejar

class DetailSpider(scrapy.Spider):
    name = 'detail'
    allowed_domains = ['movie.douban.com']
    #start_urls = ['http://movie.douban.com/']

    def start_requests(self):
        cookie = http.cookiejar.MozillaCookieJar()
        cookie.load('E:\graduation\graduation\spiders\cookie.txt', ignore_discard=True, ignore_expires=True)
        header = {
            #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Cache-Control':'max-age=0',
            'Upgrade-Insecure-Requests':'1',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'movie.douban.com',
            'Referer': 'https://accounts.douban.com/passport/login?redir=https%3A%2F%2Fmovie.douban.com%2F',
            'Cookie': 'll="118191"; bid=uBrmFJuCsfo',
        }
        client = pymongo.MongoClient(host='localhost',port=27017)
        db = client.douban
        collection = db.film_introduction
        result = collection.find({},{"movie_id":1})
        for i in result:
            movie_id = i['movie_id']
            yield scrapy.Request('https://movie.douban.com/subject/{movie_id}/'.format(movie_id=movie_id),callback=self.test,headers=header)

    def test(self,response):
        movie_name = response.css('#content h1 span::text').extract_first()
        directors = response.css('#content .grid-16-8 .attrs').extract_first()
        pattern = re.compile('.*?rel="v:directedBy">(.*?)</a>')
        director = pattern.findall(directors)
        actors = response.css('#content .grid-16-8 .actor .attrs').extract_first()
        pattern_actor = re.compile('.*?rel="v:starring">(.*?)</a>')
        actor = pattern_actor.findall(actors)
        info = response.css('#content .grid-16-8 #info').extract_first()
        pattern_type = re.compile('.*?property="v:genre">(.*?)</span>')
        movie_type = pattern_type.findall(info)
        pattern_product_area = re.compile('.*?<span class="pl">制片国家/地区:</span>(.*?)<br>')
        release_area = pattern_product_area.findall(info)
        pattern_time_detailed = re.compile('.*?<span property="v:initialReleaseDate" content="(.*?)">')
        release_time_detailed = pattern_time_detailed.findall(info)
        pattern_time = re.compile('.*?(\d{4}-\d{1,2}-\d{1,2})')
        release_time = pattern.findall(release_time_detailed[0])
        release_time = pattern_time.findall(info)
        pattern_long = re.compile('.*?<span property="v:runtime" content="(.*?)">')
        film_length = pattern_long.findall(info)
        movie_rate = response.css('#content .grid-16-8 #interest_sectl .rating_self .ll::text').extract_first()

        item = FilmDetailItem()
        item['movie_name'] = movie_name
        item['director'] = director[0]
        item['actor'] = actor
        item['movie_type'] = movie_type
        item['release_area'] = release_area[0]
        item['release_time'] = release_time[0]
        item['film_length'] = film_length[0]
        item['movie_rate'] = movie_rate
        yield item


    def parse(self, response):
        pass
