import pymongo
import pandas as pd
import re

# df = pd.read_csv(
#     'https://gist.githubusercontent.com/chriddyp/' +
#     '5d1ea79569ed194d432e56108a04d188/raw/' +
#     'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
#     'gdp-life-exp-2007.csv')
#
# print(df.continent.unique())
#
# for i in df.continent.unique():
#     x=df[df['continent'] == i]['gdp per capita']
#     y=df[df['continent'] == i]['life expectancy']
#
#     print(x)

#数据提取
# client = pymongo.MongoClient('mongodb://admin:admin123@120.79.35.73:27017/')
# db = client.douban
# collection = db.detail
# pattern = re.compile('2018')
# result = collection.find({'release_time': pattern})
# data_initial = pd.DataFrame(list(result))
#
# release_date = data_initial['release_time']
# release_date_list = []
# for i in release_date:
#     pattern_date = re.compile('.*?\d{4}-(\d{1,2}-\d{1,2})')
#     release = pattern_date.findall(i)
#     release_date_list.append(release[0])
# scatter_x = pd.Series(data=release_date_list)
#
# rate = data_initial['movie_rate']
# rate_list = []
# for i in rate:
#     rate_list.append(i)
# scatter_y = pd.Series(data=rate_list)



# Suspense = 0
# Animation = 0
# Plot = 0
# Crime = 0
# Action = 0
# Science_Fiction = 0
# Adventure = 0
# Horror = 0
# History = 0
# Funny = 0
#
# for i in type_data:
#     if '悬疑' in i:
#         Suspense += 1
#     elif '动画' in i:
#         Animation += 1
#     elif '剧情' in i:
#         Plot += 1
#     elif '犯罪' in i:
#         Crime += 1
#     elif '动作' in i:
#         Action += 1
#     elif '科幻' in i:
#         Science_Fiction += 1
#     elif '冒险' in i:
#         Adventure += 1
#     elif '惊悚' in i:
#         Horror += 1
#     elif '历史' in i:
#         History += 1
#     elif '喜剧' in i:
#         Funny += 1
#
# print(Suspense)



# data_initial = pd.DataFrame(list(collection.find()))
# del data_initial["_id"]
# data_rate_rank = data_initial.sort_values(by='movie_rate',ascending=False)
# data_rate_rank_10 = data_rate_rank[:10]
# # name = data_rate_rank_10['actor']
# # for i in range(0,10):
# #     name.values[i] = name.values[i][:2]
# # print(data_rate_rank_10)
# time = data_rate_rank_10['release_time']
# print(time.values[0])

# Jan = 0
# Feb = 0
# Mar = 0
# Apr = 0
# May = 0
# Jun = 0
# Jul = 0
# Aug = 0
# Sep = 0
# Oct = 0
# Nov = 0
# Dec = 0
# pattern = re.compile('2018')
# result = collection.find({'release_time': pattern})
# data_initial = pd.DataFrame(list(result))
# month_data = data_initial['release_time']
# for i in month_data:
#     pattern_month = re.compile('\d{4}-(\d{1,2})-\d{1,2}')
#     number = pattern_month.findall(i)
#     if number[0] == '01':
#         Jan += 1
#     elif number[0] == '02':
#         Feb += 1
#     elif number[0] == '03':
#         Mar += 1
#     elif number[0] == '04':
#         Apr += 1
#     elif number[0] == '05':
#         May += 1
#     elif number[0] == '06':
#         Jun += 1
#     elif number[0] == '07':
#         Jul += 1
#     elif number[0] == '08':
#         Aug += 1
#     elif number[0] == '09':
#         Sep += 1
#     elif number[0] == '10':
#         Oct += 1
#     elif number[0] == '11':
#         Nov += 1
#     elif number[0] == '12':
#         Dec += 1
#
# # print('''
# #     一月:{}
# #     二月:{}
# #     三月:{}
# #     四月:{}
# #     五月:{}
# #     六月:{}
# #     七月:{}
# #     八月:{}
# #     九月:{}
# #     十月:{}
# #     十一月:{}
# #     十二月:{}
# # '''.format(Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec))
# data = {
#     'Jan':Jan,'Feb':Feb,'Mar':Mar,'Apr':Apr,'May':May,'Jun':Jun,'Jul':Jul,'Aug':Aug,'Sep':Sep,'Oct':Oct,'Nov':Nov,'Dec':Dec
# }
# df = pd.DataFrame(data, index=list(['num']))
# x = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# y = [Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec]
# print(y)

# client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
# db = client.douban
# collection = db.detail
# pattern = re.compile('20')
# result = collection.find({'release_time': pattern})
# data_initial = pd.DataFrame(list(result))
# # X轴
# release_date = data_initial['release_time']
# release_date_list = []
# for i in release_date:
#     release_date_list.append(i)
# scatter_x = pd.Series(data=release_date_list)
# # Y轴
# rate = data_initial['movie_rate']
# rate_list = []
# for i in rate:
#     rate_list.append(i)
# scatter_y = pd.Series(data=rate_list)
# print(scatter_x)
# print(scatter_y)

client = pymongo.MongoClient(host='localhost',port=27017)
db = client.douban
collection = db.film_introduction
result = collection.find({},{"movie_id":1})
for i in result:
    print(i['movie_id'])
