# -*- coding: utf-8 -*-
import scrapy
import re
from graduation.items import FilmDetailItem
import pymongo
from graduation.settings import MONGO_URI,MONGO_DB

class DetailSpider(scrapy.Spider):
    name = 'detail'
    allowed_domains = ['movie.douban.com']
    #start_urls = ['http://movie.douban.com/']

    def start_requests(self):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/annual/2018',
        }
        client = pymongo.MongoClient('mongodb://admin:admin123@120.79.35.73:27017/')
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
        pattern_time = re.compile('.*?<span property="v:initialReleaseDate" content="(.*?)">')
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
        item['release_time'] = release_time
        item['film_length'] = film_length[0]
        item['movie_rate'] = movie_rate
        yield item


    def parse(self, response):
        pass
