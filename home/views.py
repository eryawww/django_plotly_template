from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go

def home(request):
    def scatter():
        x1 = [1, 2, 3, 4]
        y1 = [30, 35, 25, 45]

        trace = go.Scatter(
            x=x1,
            y = y1
        )
        layout = go.Layout(
            height=450,
            title='Simple Graph',
            xaxis=dict(range=[min(x1), max(x1)]),
            yaxis = dict(range=[min(y1), max(y1)]),
            # paper_bgcolor='#27293d', 
            # plot_bgcolor='rgba(0,0,0,0)',
            # font=dict(color='white'),
            margin=dict(l=50, r=50, t=30, b=0),
        )

        fig = go.Figure(data=[trace], layout=layout)
        plot_div = plot(fig, output_type='div')
        return plot_div

    context ={
        'plot': scatter()
    }

    return render(request, 'home.html', context)