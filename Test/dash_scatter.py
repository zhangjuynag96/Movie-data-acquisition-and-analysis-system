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

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout=html.Div([
    html.Div(id='x')
])

@app.callback(Output('x','children'),)
def update_output_scatter():
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
    #     release_date_list.append(i)
    # scatter_x = pd.Series(data=release_date_list)
    #
    # rate = data_initial['movie_rate']
    # rate_list = []
    # for i in rate:
    #     rate_list.append(i)
    # scatter_y = pd.Series(data=rate_list)
    client = pymongo.MongoClient('mongodb://admin:admin123@120.79.35.73:27017/')
    db = client.douban
    collection = db.detail
    pattern = re.compile('2018')
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
            # figure={
            #     'data':[
            #         go.Scatter(
            #             x = scatter_x,
            #             y = scatter_y,
            #             mode='markers',
            #         )
            #     ],
            #     'layout': go.Layout(
            #         xaxis={'title': 'Movie analyse'},
            #         yaxis={'title': 'Movies Number'},
            #     )
            # }
                figure={
                    'data': [
                        dict(
                            type='pie', name='Pie',
                            labels=['悬疑', '动画', '剧情', '犯罪', '动作', '科幻', '冒险', '惊悚', '历史', '喜剧'],
                            values=[Suspense, Animation, Plot, Crime, Action, Science_Fiction, Adventure, Horror, History,
                                    Funny]
                        )
                    ],
                    'layout': {
                        'title': '饼图'
                    }
                }
        )




if __name__ == '__main__':
    app.run_server(debug=True)