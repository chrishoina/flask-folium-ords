# Use this as the starting location: 35.78742648626059, -78.78122033558192
# Eventually we'll use the " class folium.plugins.LocateControl(auto_start=False, **kwargs)" plug-in to automatically detect a user's location" 

import json
from pandas import read_stata
import requests
import folium
import altair as alt 
from folium import Popup, plugins, features

#adding ".json()" to the end of this request will treat it differently; as a json object. It will treat the response as a json dictionary. 
m = folium.Map(location=[35.78742648626059, -78.78122033558192], zoom_start=12, tiles="Stamen Toner")

reats = requests.get('https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/eats/').json()

# rexams = requests.get('https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/examsscores/').json()

# r2 = requests.get('https://restcountries.com/v3.1/all').json()

r1 = reats['items']

for stream1 in r1:

    if stream1:
        lat = stream1['y']
        long = stream1['x']
        name = stream1['name']
        id = stream1['hsisid']
   
        folium.Marker(location=[lat,long], popup = folium.Popup('<i>{}</i>'.format(id))).add_to(m)

        data = alt.Data(values=stream1)  
      
        main = alt.Chart(data).mark_point(color='#6d4c41').encode(alt.X('date_:T', title='Year'), alt.Y('score:Q', title='Score', scale=alt.Scale(zero=False))).properties(title='Health Score')


    else:
        continue 

        
#         folium.Marker(location=[lat,long], popup = folium.Popup('<i>{}</i>'.format(name))).add_to(m)

#     else:
#         continue 
        # line = alt.Chart(data).mark_line(color='#9575cd').transform_window(
        # # The field to average
        # rolling_mean='mean(score)',
        # # The number of values before and after the current value to include.
        # frame=[-9, 0]).encode(x='date_:T', y='rolling_mean:Q')

        # (main + line).properties(width=600, height=350, padding=15).configure_title(fontSize=40, font='Andale Mono',align='center',color='#263238').configure_axis(titleColor='#263238', titleFont='Andale Mono', labelFont='Andale Mono', labelColor='#263238', grid=False).configure_view(strokeWidth=0)




#     print(type(r))
#     print(r['hsisid'])
#     print(type(r['hsisid']))
#     print(type(r['name']))
#     print(r['name'])
#     print(r['x'])
#     print(r['y'])
# print(dict.keys(r1))
# print(dict.values(r1)[0])

# for values in r1:
#     print(range(len('hsisid')))

# for items in r1:
#     print(items)
#     print(items('items'))


# dfa=pd.DataFrame(r1['items'])
# dfb = dfa.loc[:, ("hsisid", "name", "x", "y")]
# dfb.info()
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



# for 
# iter_modules
# iterro

# folium.Marker(location=[35.78742648626059, -78.78122033558192]
# # [df['y'], df['x']]
# , popup = folium.Popup('<i>{}</i>'.format(df['name']))).add_to(m)


# # # print(Resty)  
# # # print(hsisid)  
# # plugins.LocateControl().add_to(m)
m.save("index.html")

