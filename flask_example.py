""" flask_example.py

    Required packages:
    - flask
    - folium

    Usage:

    Start the flask server by running:

        $ python flask_example.py

    And then head to http://127.0.0.1:5000/ in your browser to see the map displayed

"""
# STEP 1: 
    # To activate flask: ". venv/bin/activate"
    # *** Make sure there is a space between the period and venv *** 

# STEP 2:
    # "export FLASK_ENV=development"
    # "export FLASK_APP=[app name]"
    #       *** This should work, as long as you created a module (to be imported when "flask run" is entered). In this case it would be the "app = Flask(__name__)"" line of code
    # flask run

from flask import Flask, Markup 
import requests
import json
import folium
from folium import JavascriptLink 

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
                # .add_child(
                #     folium.Vega(datafromjson, width=450, height=250)
                #     ),
            ).add_to(folium_map)
        else:
            continue
    folium_map.get_root().html.add_child(JavascriptLink('./static/app.js'))        

    #  # get definition of map in body
    # html_map = folium_map._repr_html_() 
    # map_div = Markup(folium_map.get_root().html.render())

    # # html to be included in header
    # hdr_txt = Markup(folium_map.get_root().header.render())

    # # html to be included in <script>
    # script_txt = Markup(folium_map.get_root().script.render()) 

    # print(script_txt) 
    # print('hello world')
    
    return html_map

@app.route('/data/<id>')
def get_data(id):
    # id = 4092018434
    rscores = (f"https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/examscores/?q={{\"hsisid\":{id}}}")
    r = requests.get(rscores).json()


    return r

if __name__ == '__main__':
    app.run(debug=True)





