
import altair as alt

# from vega_datasets import data
import requests
import json
# url = data.cars.url

# alt.Chart(url).mark_point().encode(
#     x='Horsepower:Q',
#     y='Miles_per_Gallon:Q'
# )

url = ('https://gf641ea24ecc468-dbmcdeebyface.adb.us-ashburn-1.oraclecloudapps.com/ords/pythondev/exam_scores/?q={%22hsisid%22:4092015191}').json()

r = json.loads(requests.get(url))
print(r)

data = alt.Data(values=r['items'])
# print(data)
# print(r.json()) 
# print(type(r.json()))
for i in r.iter_content():
    print(i)
    print(r["items:"])
print(type(r))
data = alt.Data.from_json(r)
print(data)

# #reference for Oracle APEX colors - https://www.oracle.com/webfolder/technetwork/jet/jetCookbook.html?component=colorPalette&demo=paletteGridSwatchSizes

main = alt.Chart(data).mark_point(color='#6d4c41').encode(
    alt.X('date_:T', title='Year'), alt.Y('score:Q', title='Score', scale=alt.Scale(zero=False))
).properties(
        # width=500, height=150, 
        # padding=10,
    title='ur helf skorz'
)

# line = alt.Chart(data).mark_line(color='#9575cd').transform_window(
#     # The field to average
#     rolling_mean='mean(score)',
#     # The number of values before and after the current value to include.
#     frame=[-9, 0]
# ).encode(
#     x='date_:T',
#     y='rolling_mean:Q'
# )

# (main + line).properties(width=600, height=350, padding=15
# ).configure_title(
#     fontSize=40, 
#     font='Andale Mono',
#     align='center',
#     color='#263238'
# ).configure_axis(titleColor='#263238', titleFont='Andale Mono', labelFont='Andale Mono', labelColor='#263238', grid=False
# ).configure_view(strokeWidth=0)

# # print(r)
#     # for items in r:
#     #     pddata = r['items']

#     # data = pd.DataFrame(pddata)

#     # chart = alt.Chart(data).mark_line().encode(
#     #     x='date_:T',
#     #     y='score:Q'
#     #     )

#     # # chart.save('test.html')

