# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pymongo
import re

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
x = 0
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
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
    #dcc.Input(id='input-1-state', type='text', value='Montréal'),
    #dcc.Input(id='input-2-state', type='text', value='Canada'),
    #html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])


@app.callback(Output('output-state', 'children'),
              [Input('choice', 'value')])
def update_output(Input):
    client = pymongo.MongoClient('mongodb://admin:admin123@120.79.35.73:27017/')
    db = client.douban
    collection = db.detail
    pattern = re.compile(Input)
    result = collection.find({'release_time':pattern})
    for i in result:
        print(i)


if __name__ == '__main__':
    app.run_server(debug=True)