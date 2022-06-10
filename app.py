# ".venv/bin/activate"
# "export FLASK_ENV=development"
# "export FLASK_APP=[app name]"
# flask run

import json
from flask import Flask, request_started, url_for
from numpy import source
from pyrsistent import l
import requests
import folium
import altair as alt
from folium import Popup, plugins, features, JavascriptLink
import branca



# ------------------------------------------------------------------- #
# I checked to make sure this runs, you should be able to, just to see what the example chart looks like. Its very generic, but the scaling/height/width/etc. can all be changed. This is what would be added to the existing marker. 

# import json, requests
# import altair as alt 

# id = 4092018375
# scores = requests.get(f"https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/examscores/?q={{\"hsisid\":{id}}}").json()

# print(scores)
# data = alt.Data(values=scores['items']) 
    
# mychart = alt.Chart(data).mark_point().encode(
# alt.X('date_:T', title='Time'), alt.Y('score:Q', title='Score')
# ).properties(title='Health Scores')

# mychart 

# ------------------------------------------------------------------- #

app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (35.78742648626059, -78.78122033558192)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    reats = requests.get('https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/eats/').json()
    r1 = reats['items']
    for stream1 in r1:
        if stream1:
            lat = stream1['y']
            long = stream1['x']
            id = stream1['hsisid']
            # print(id)
            folium.Marker(
                location=[lat,long], popup = folium.Popup('<i onclick="getchart({})">Click for Scores</i>'.format(id))
            ).add_to(folium_map)
        else:
            continue
    folium_map.get_root().html.add_child(JavascriptLink('./static/jsfunctions.js'))        

# For some reason, this is broken in my flask app, its no longer working. I had to move some things around when I was cleaning up. There is a good chance I didn't copy/paste something over. I compared it to previous versions (this and the .js file) but I don't see where the error/issue is. 

# I found another reference in the folium github that might be good to look at too. It has to do with adding an altair chart to a pop-up. This is probably better than me explaining, since it has an actual working example: https://github.com/python-visualization/folium/issues/1239


    return folium_map._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)

    # This is the link to the GitHub issue that references the below lines (69-82): https://github.com/python-visualization/folium/issues/1223

    #  # get definition of map in body
    # html_map = folium_map._repr_html_() 
    # map_div = Markup(folium_map.get_root().html.render())

    # # html to be included in header
    # hdr_txt = Markup(folium_map.get_root().header.render())

    # # html to be included in <script>
    # script_txt = Markup(folium_map.get_root().script.render()) 

    # print(script_txt) 
    # print('hello world')
    
    # return folium_map.render

@app.route('/data/<id>')
def get_data(id):
    scores = (f"https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/examscores/?q={{\"hsisid\":{id}}}")
    response = requests.get(scores).json()

    return response 

# I'm not sure if this route above ^^^ is where the "adding to existing marker" occuers. In the folium documentation, it looks like everything is named/given first, then the map is rendered. But I don't see anything that is done iteratively. 

# The "onclick" event should trigger flask/folium (not sure which is actually doing the work) to render an Altair chart for the assosciated "HSIS ID".

# If you run the code in lines 18-36, in the "interactive window", you'll see that it does work. In the folium documentation, the way to add a chart to an existing marker is as such: 

# 1. You create the map (with starting lat/long), like:
#     m = folium.Map(location=[46.3014, -123.7390], zoom_start=7, tiles="Stamen Terrain")

# 2. Create the marker + popup
# folium.Marker(
#     location=[44.639, -124.5339],
#     popup=folium.Popup(max_width=450).add_child(
#         folium.Vega(mychart, width=450, height=250)
#     ),
# ).add_to(m)

#in this case, "mychart" is the same one that I would have identified in lines 18-36. 







