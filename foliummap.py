# Use this as the starting location: 35.78742648626059, -78.78122033558192
# Eventually we'll use the " class folium.plugins.LocateControl(auto_start=False, **kwargs)" plug-in to automatically detect a user's location" 

import json
from pkgutil import iter_modules
from pydoc import locate
from sqlite3 import Row
from textwrap import indent
from tkinter import Y
import requests
import folium
import altair as alt 
import pandas as pd
import numpy as np
from folium import plugins

# url = 'https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/exam_scores/?q={%22hsisid%22:4092015191}'

# r = requests.get(url).json()
# for items in r:
#     pddata = r['items']

# data = pd.DataFrame(pddata)

# chart = alt.Chart(data).mark_line().encode(
#     x='date_:T',
#     y='score:Q'
#     )


r1 = requests.get('https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/eats/').json()
# r2 = requests.get('https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/eats/')
# # print(r1)
# x=r2.json() 

dfa=pd.DataFrame(r1['items'])
dfb = dfa.loc[:, ("hsisid", "name", "x", "y")]
dfb.info()
# print(df.dtypes)
# print(df['y'].dtype)
# print(df['x'].dtype)
# print(df['column_1'])

# print(df)
# print(type(df))
# df2 = pd.read_json(x['items'].text)
# print(df2)
# df = pd.DataFrame(
#         for entry in r1['items']:
#         resty = entry['name']
#         hsisid = entry['hsisid']
#         lat = entry['y']
#         long = entry['x']
# )


m = folium.Map(location=[35.78742648626059, -78.78122033558192], zoom_start=12, tiles="Stamen Toner")
for 
iter_modules
iterro

folium.Marker(location=[35.78742648626059, -78.78122033558192]
# [df['y'], df['x']]
, popup = folium.Popup('<i>{}</i>'.format(df['name']))).add_to(m)


# # print(Resty)  
# # print(hsisid)  
# plugins.LocateControl().add_to(m)
m.save("index.html")

