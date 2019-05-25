import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from pandas import DataFrame
import numpy as np
from sklearn import datasets
import pymongo
from dash.dependencies import Input, Output, State
import re

#-------------------------------------------------------------------------------------------------------
#数据传入
# df = pd.read_csv(
#     'https://gist.githubusercontent.com/chriddyp/' +
#     '5d1ea79569ed194d432e56108a04d188/raw/' +
#     'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
#     'gdp-life-exp-2007.csv')

#连接数据库
client = pymongo.MongoClient(host='localhost',port=27017)
db = client.douban
collection = db.detail

#榜单排名
# data_initial = pd.DataFrame(list(collection.find()))
# del data_initial["_id"]
# del data_initial["director"]
# del data_initial["release_area"]
# data_rate_rank = data_initial.sort_values(by='movie_rate',ascending=False)
# data_rate_rank_10 = data_rate_rank[:10]
# name = data_rate_rank_10['actor']
# time = data_rate_rank_10['release_time']
# for i in range(0,10):
#     name.values[i] = name.values[i][:2]
#     time.values[i] = time.values[i][:1]
# data_rate_rank_10.columns = ['演员','电影时长','电影名称','电影评分','电影类型','上映时间']
# data_rate_rank_10['排名'] = [1,2,3,4,5,6,7,8,9,10]
# data_rate_rank_10 = data_rate_rank_10[['排名','电影名称','演员','电影类型','上映时间','电影时长','电影评分']]


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#--------------------------------------------------------------------------------------------------------------------------------------
#数据交互方法

#自动生成排名前十的榜单
# def generate_table(dataframe, max_rows=10):
#     return html.Table(
#         # Header
#         [html.Tr([html.Th(col) for col in dataframe.columns])] +
#
#         # Body
#         [html.Tr([
#             html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#         ]) for i in range(min(len(dataframe), max_rows))]
#     )
#----------------------------------------------------------------------------------------------------------------------------------------
#前端页面构建

app.layout=html.Div([

    #导航栏
    html.Div([
        html.Div([
            html.Div([html.H1(children='G',style={'color':'#fff'})],style={'width':'2.5%','float':'left'}),
            html.Div([html.H6(children=' Movie analyse system',style={'color':'#fff','font-family':'Arial'})],style={'float':'left','padding-top':'12px'}),
            html.Div([html.H6(children='黄山学院',style={'color':'#fff'})],style={'float':'right','padding-top':'12px'}),
        ],style={'backgroundColor':'#303030','height':'65px'}),
    ]),
    #选择框
    html.Div([
        html.Div([
            html.Div([
                dcc.Dropdown(
                id = 'choice',
                options=[
                    {'label': '全部', 'value': '20'},
                    {'label': '2009', 'value': '2009'},
                    {'label': '2010', 'value': '2010'},
                    {'label': '2011', 'value': '2011'},
                    {'label': '2012', 'value': '2012'},
                    {'label': '2013', 'value': '2013'},
                    {'label': '2014', 'value': '2014'},
                    {'label': '2015', 'value': '2015'},
                    {'label': '2016', 'value': '2016'},
                    {'label': '2017', 'value': '2017'},
                    {'label': '2018', 'value': '2018'},
                    {'label': '2019', 'value': '2019'},
                ],
                value='20'
                ),
            ]),
        ]),
    ]),


    html.Div([
        #榜单排名
        html.Div([
            html.H4(children='电影评分排名'),
            html.Div(id='rank_10',style={'font-size':'3px','border':'slide'}),
        ],style={'float':'left','width':'48%','height':'700px','border':'6px solid #DCDCDC'}),

        #散点图
        html.Div([
            html.Div([html.H4(children='电影数据散点图')]),
            html.Div(id='scatter'),
        ],style={'float':'left','width':'48%','height':'700px','border':'6px solid #DCDCDC'}),

        #线图
        html.Div([
            html.H4(children='电影产量折线图'),
            html.Div(id='line')
        ],style={'width':'48%','height':'700px','float':'left','border':'6px solid #DCDCDC'}),

        #饼图
        html.Div([
            html.H4(children='电影类型饼图'),
            html.Div(id='pie')
        ],style={'width':'48%','height':'700px','float':'left','border':'6px solid #DCDCDC'})

    ],style={'padding':'10px'}),

],style={'bgcolor':'#DCDCDC'})

#生成前10榜单
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

@app.callback(Output('rank_10', 'children'),
               [Input('choice', 'value')])
def update_output_div(Input,max_rows=10):
    # client = pymongo.MongoClient('mongodb://admin:xxx@120.79.35.73:27017/')
    # db = client.douban
    collection = db.detail
    pattern = re.compile(Input)
    result = collection.find({'release_time': pattern})
    data_initial = pd.DataFrame(list(result))
    del data_initial["_id"]
    del data_initial["director"]
    del data_initial["release_area"]
    data_rate_rank = data_initial.sort_values(by='movie_rate', ascending=False)
    data_rate_rank_10 = data_rate_rank[:10]
    name = data_rate_rank_10['actor']
    time = data_rate_rank_10['release_time']
    for i in range(0, 10):
        name.values[i] = name.values[i][:2]
        time.values[i] = time.values[i]
    data_rate_rank_10.columns = ['演员', '电影时长', '电影名称', '电影评分', '电影类型', '上映时间']
    data_rate_rank_10['排名'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data_rate_rank_10 = data_rate_rank_10[['排名', '电影名称', '演员', '电影类型', '上映时间', '电影时长', '电影评分']]
    return generate_table(data_rate_rank_10)

#生成散点图
@app.callback(Output('scatter','children'),
              [Input('choice', 'value')])
def update_output_scatter_marker(Input):
    # client = pymongo.MongoClient('mongodb://admin:xxx@120.79.35.73:27017/')
    # db = client.douban
    collection = db.detail
    pattern = re.compile(Input)
    result = collection.find({'release_time': pattern})
    data_initial = pd.DataFrame(list(result))
    #X轴
    release_date = data_initial['release_time']
    release_date_list = []
    for i in release_date:
        release_date_list.append(i)
    scatter_x = pd.Series(data=release_date_list)
    #Y轴
    rate = data_initial['movie_rate']
    rate_list = []
    for i in rate:
        rate_list.append(i)
    scatter_y = pd.Series(data=rate_list)

    return dcc.Graph(
        figure={
            'data':[
                go.Scatter(
                    x = scatter_x,
                    y = scatter_y,
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 10,
                        'line': {'width': 0.5, 'color': 'white'}
                    }
                )
            ],
            'layout': go.Layout(
                xaxis={'title': '上映时间'},
                yaxis={'title': '电影评分'},
            )
        }
    )

#生成折线图
@app.callback(Output('line','children'),
              [Input('choice', 'value')])
def update_output_line(Input):
    # client = pymongo.MongoClient('mongodb://admin:xxx@120.79.35.73:27017/')
    # db = client.douban
    collection = db.detail
    # Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec = 0
    Jan = 0
    Feb = 0
    Mar = 0
    Apr = 0
    May = 0
    Jun = 0
    Jul = 0
    Aug = 0
    Sep = 0
    Oct = 0
    Nov = 0
    Dec = 0
    pattern = re.compile(Input)
    result = collection.find({'release_time': pattern})
    data_initial_time = pd.DataFrame(list(result))
    month_data = data_initial_time['release_time']
    for i in month_data:
        pattern_month = re.compile('\d{4}-(\d{1,2})-\d{1,2}')
        number = pattern_month.findall(i)
        if number[0] == '01':
            Jan += 1
        elif number[0] == '02':
            Feb += 1
        elif number[0] == '03':
            Mar += 1
        elif number[0] == '04':
            Apr += 1
        elif number[0] == '05':
            May += 1
        elif number[0] == '06':
            Jun += 1
        elif number[0] == '07':
            Jul += 1
        elif number[0] == '08':
            Aug += 1
        elif number[0] == '09':
            Sep += 1
        elif number[0] == '10':
            Oct += 1
        elif number[0] == '11':
            Nov += 1
        elif number[0] == '12':
            Dec += 1
    x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    y = [Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec]

    return dcc.Graph(
        figure={
            'data':[
                {'x':x,'y':y,'type':'Scatter','name':'Line'},
            ],
            'layout':{
                'title':'线图'
            }
        }
    )

#生成饼图
@app.callback(Output('pie','children'),
              [Input('choice', 'value')])
def update_output_pie(Input):
    # client = pymongo.MongoClient('mongodb://admin:xxx@120.79.35.73:27017/')
    # db = client.douban
    collection = db.detail
    pattern = re.compile(Input)
    result = collection.find({'release_time': pattern})
    data_initial = pd.DataFrame(list(result))
    type_data = data_initial['movie_type']

    Suspense = 0
    Animation = 0
    Plot = 0
    Crime = 0
    Action = 0
    Science_Fiction = 0
    Adventure = 0
    Horror = 0
    History = 0
    Funny = 0

    for i in type_data:
        if '悬疑' in i:
            Suspense += 1
        elif '动画' in i:
            Animation += 1
        elif '剧情' in i:
            Plot += 1
        elif '犯罪' in i:
            Crime += 1
        elif '动作' in i:
            Action += 1
        elif '科幻' in i:
            Science_Fiction += 1
        elif '冒险' in i:
            Adventure += 1
        elif '惊悚' in i:
            Horror += 1
        elif '历史' in i:
            History += 1
        elif '喜剧' in i:
            Funny += 1
    return dcc.Graph(
        figure={
            'data':[
                dict(
                    type='pie', name='Pie',
                    labels = ['悬疑','动画','剧情','犯罪','动作','科幻','冒险','惊悚','历史','喜剧'],
                    values = [Suspense,Animation,Plot,Crime,Action,Science_Fiction,Adventure,Horror,History,Funny]
                )
            ],
            'layout':{
                'title':'饼图'
            }
        }
    )













#---------------------------------------------------------------------------------------------------------------------------------
#主程序入口
if __name__ == '__main__':
    app.run_server(debug=True)