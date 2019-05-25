import requests
import re
header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/annual/2018',
        }
result = requests.get('https://movie.douban.com',headers=header)
print(result)
# pattern_time = re.compile('.*?<span property="v:initialReleaseDate" content="(.*?)">')
# release_time = pattern_time.findall(result.text)
# print(release_time[0])
# pattern = re.compile('.*?(\d{4}-\d{1,2}-\d{1,2})')
# x = pattern.findall(release_time[0])
# print(x)

# import pymongo
#
# client = pymongo.MongoClient('mongodb://admin:admin123@120.79.35.73:27017/')
# db = client.douban
# collection = db.film_introduction
# result = collection.find({},{"movie_id":1})
# for i in result:
#     print(i['movie_id'])