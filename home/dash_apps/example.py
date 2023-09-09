from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = DjangoDash('example', external_stylesheets=external_stylesheets)
app.layout = html.Div(
    children=[
        dcc.Dropdown(
            id='columns', 
            options=[{'label': i, 'value': i} for i in range(10)],
            value=2
        ),
        dcc.Graph(id='scatter-plot')
    ]
)
@app.callback(
    Output(component_id='scatter-plot', component_property='figure'), 
    Input(component_id='columns', component_property='value')
)
def update_graph(value):
    x, y = [], []
    for i in range(value):
        x.append(i)
        y.append(i)
    graph = go.Scatter(x=x, y=y, name='EXAMPLE')
    layout = go.Layout(
        # width=600,
        # height=700,
        # autosize=True,
        # paper_bgcolor='#27293d', 
        # plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[min(x), max(x)]),
        yaxis=dict(range=[min(y), max(y)]),
        font=dict(color='white'),
        # margin=dict(l=50, r=50, t=25, b=0),
    )
    return {'data': [graph], 'layout': layout}