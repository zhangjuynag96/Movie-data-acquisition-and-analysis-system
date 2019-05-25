# for type in range(1,30):
#     print('https://movie.douban.com/ithil_j/activity/movie_annualyears/widget/{type}'.format(type=str(type)))
#import random
# tags = ['是','说']
# for tag in tags:
#     print(tag)
# tags = ['热门','最新','经典','可播放','豆瓣高分','冷门佳片','华语','欧美','韩国','日本','动作','喜剧','爱情','科幻','悬疑','恐怖','治愈']
# for tag in tags:
#     for i in range(15):
#         page = i * 20
#         print(tag)
#         print(page)
#import pymongo
#from graduation.settings import MONGO_DB,MONGO_URI

#client = pymongo.MongoClient(host=MONGO_URI,port=27017)
#db = client.douban
#collection = db.film_introduction
#result = collection.find({},{"movie_id":1})
#for i in result:
#    print(i['movie_id'])

import requests
header = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'keep-alive',
            'Host':'movie.douban.com',
            'Referer':'https://movie.douban.com/annual/2018',
        }
proxy = {"http" : "180.118.135.216:9999"}
x = requests.get('https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start=0',headers=header,proxies=proxy)
print(x.text)
