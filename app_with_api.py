# Made a venv - real python, virtual environments, a primer
# https://realpython.com/python-virtual-environments-a-primer/

from operator import itemgetter
import requests

station_names = ['Ponsanooth', 'Brent (Monks Park)', 'Armley', 'Banks Road', 'Victoria Mill']
station_references = ['48183', '3850TH', 'F1707', 'E1488', 'E1901']

readings = []

for i in station_references[0:2]:
    api_url = "https://environment.data.gov.uk/hydrology/data/readings.json?station.stationReference={}&latest&_limit=1".format(i)
    try:
        response = requests.get(api_url)
    except:
        continue
    else:
        value = response.json()['items'][0]['value']
        readings.append(value)


#print(len(readings), len(station_names[0:2]))


# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Insert API here



# Might need to wait for API to return before showing the plot

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.DataFrame({
    "Station": station_names[0:2],
    "Amount": readings,
    "City": ["SF", "SF"]
})

fig = px.bar(df, x="Station", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
