# -*- coding: utf-8 -*-
import scrapy
import jsonpath_rw_ext
import json
from graduation.items import FilmIntroductionItem
from scrapy import Request

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']

    def start_requests(self):
        header = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'keep-alive',
            'Host':'movie.douban.com',
            'Referer':'https://movie.douban.com/annual/2018',
        }
        tags = ['热门','最新','经典','可播放','豆瓣高分','冷门佳片','华语','欧美','韩国','日本','动作','喜剧','爱情','科幻','悬疑','恐怖','治愈']
        for tag in tags:
            for i in range(15):
                page = i * 20
                yield Request('https://movie.douban.com/j/search_subjects?type=movie&tag={tag}&sort=recommend&page_limit=20&page_start={page}'.format(tag=tag,page=page),headers=header,callback=self.test)

    def test(self,response):
        #print(response.text)
        html = json.loads(response.text)
        rate = jsonpath_rw_ext.match('$..rate',html)
        title = jsonpath_rw_ext.match('$..title',html)
        id = jsonpath_rw_ext.match('$..id',html)
        for i in range(0,len(rate)):
            item = FilmIntroductionItem()
            item['movie_rate'] = rate[i]
            item['movie_name'] = title[i]
            item['movie_id'] = id[i]
            yield item

    def parse(self, response):
        pass
