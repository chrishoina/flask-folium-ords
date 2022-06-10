# STEP 1: 
    # To activate flask: ". venv/bin/activate"
    # *** Make sure there is a space between the period and venv *** 

# STEP 2:
    # "export FLASK_ENV=development"
    # "export FLASK_APP=[app name]"
    #       *** This should work, as long as you created a module (to be imported when "flask run" is entered). In this case it would be the "app = Flask(__name__)"" line of code
    # flask run

import json
from flask import request_started
from numpy import source
import requests
import folium
import altair as alt
from folium import Popup, plugins, features
import branca


id = 4092018375
scores = requests.get(f"https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/examscores/?q={{\"hsisid\":{id}}}").json()

data = alt.Data(values=scores['items'])

    
chart = alt.Chart(data).mark_point(opacity=0.2, color='red').encode(
alt.X('date_:T', title='Year'), alt.Y('score:Q', title='Score', scale=alt.Scale(zero=False))
).properties(
# width=500, height=150, 
# padding=10,
title='Health Scores')

m = folium.Map(location=[35.78742648626059, -78.78122033558192], zoom_start=12, tiles="Stamen Toner")

eats = requests.get('https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/eats/').json()

requests1 = eats['items']
for payload in requests1:

    lat = payload['y']
    long = payload['x']
    id = payload['hsisid']

    folium.Marker(
        location=[lat,long], 
        popup = folium.Popup('<i onclick="window.alert(\'Hello World{}\')">Click for Details</i>'.format(id))

    ).add_to(m)
# m.save("index.html")



m.add_child(chart) 
m.save("index.html")


