# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import plotly.graph_objs as go
# import pandas as pd
# import pymongo

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
#
#
# app.layout = html.Div([
#     html.Div(id='line')
# ])
#
# x = ['a','b','c','d']
# y = [5,6,12,8]
#
# @app.callback(
#     Output('line','children')
# )
# def update_output_div():
#     return dcc.Graph(
#         figure={
#             'data':[
#                 {'x':x,'y':y,'type':'Scatter','name':'Line'},
#             ],
#             'layout':'线图'
#         }
#     )
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
#
# @app.callback(
#     Output(component_id='my-div', component_property='children'),
#     [Input(component_id='my-id', component_property='value')]
# )
#
# def update_output_div(input_value,max_rows=10):
#     client = pymongo.MongoClient('mongodb://admin:admin123@120.79.35.73:27017/')
#     db = client.douban
#     collection = db.detail
#     data_initial = pd.DataFrame(list(collection.find()))
#     del data_initial["_id"]
#     del data_initial["director"]
#     del data_initial["release_area"]
#     data_rate_rank = data_initial.sort_values(by='movie_rate', ascending=False)
#     data_rate_rank_10 = data_rate_rank[:10]
#     name = data_rate_rank_10['actor']
#     time = data_rate_rank_10['release_time']
#     for i in range(0, 10):
#         name.values[i] = name.values[i][:2]
#         time.values[i] = time.values[i][:1]
#     data_rate_rank_10.columns = ['演员', '电影时长', '电影名称', '电影评分', '电影类型', '上映时间']
#     data_rate_rank_10['排名'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     data_rate_rank_10 = data_rate_rank_10[['排名', '电影名称', '演员', '电影类型', '上映时间', '电影时长', '电影评分']]
#     return generate_table(data_rate_rank_10)



# if __name__ == '__main__':
#     app.run_server(debug=True)

import dash
import dash_core_components
import dash_html_components
import numpy as np
from sklearn import datasets
import pandas as pd
import plotly.figure_factory as ff

# iris = datasets.load_iris()
# data = pd.DataFrame(iris.data, columns=['SpealLength', 'Spealwidth',
#                                         'PetalLength', 'PetalLength'])
# data = data[:30]
#
# app = dash.Dash()
#
# def test5(app, data):

    # data['group1'] = data['SpealLength'].apply(lambda x: int(x))
    # print(data['group1'])
    # tmp = data.groupby('group1').size().to_frame()
    # tmp = tmp.rename(columns={0: 'num'})
    # tmp = np.round(tmp, 4).reset_index(drop=False)
    # print(tmp)
    #
    # app.layout = dash_html_components.Div(children=[
    #     dash_html_components.H1(children='Demo'),
    #     dash_core_components.Graph(
    #         id='pie',
    #         figure={
    #             'data': [
    #                 dict(
    #                     type='pie', name='Pie',
    #                     labels=tmp['group1'].tolist(),
    #                     values=tmp['num'].tolist(),
    #                 )
    #             ],
    #             'layout': {
    #                 'title': '饼图'
    #             }
    #         }
    #     )
    # ])

# test5(app, data)
# # app.run_server(debug=True)

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

# df = pd.read_csv(
#     'https://gist.githubusercontent.com/chriddyp/' +
#     '5d1ea79569ed194d432e56108a04d188/raw/' +
#     'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
#     'gdp-life-exp-2007.csv')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout=html.Div([
    html.Div([html.H4(children='电影数据散点图')], style={'padding-bottom': '20px'}),
    html.Div(id='scatter'),
    ])

@app.callback(Output('scatter','children'),
              )
def update_output_scatter_marker(Input):
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
    db = client.douban
    collection = db.detail
    pattern = re.compile('20')
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

if __name__ == '__main__':
    app.run_server(debug=True)