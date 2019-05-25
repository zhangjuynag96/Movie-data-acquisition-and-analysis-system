# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class GraduationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class FilmIntroductionItem(scrapy.Item):
    collection = table = 'film_introduction'
    movie_rate = Field() # 电影评分
    movie_name = Field() # 电影名称
    movie_id = Field() #电影id

class FilmDetailItem(scrapy.Item):
    collection = table = 'detail'
    movie_name = Field() #电影名称
    director = Field() #导演
    actor = Field() #演员
    movie_type = Field() #电影类型
    release_area = Field() #上映区域
    release_time = Field() #上映时间
    film_length = Field() #电影片长
    movie_rate = Field() #电影评分
