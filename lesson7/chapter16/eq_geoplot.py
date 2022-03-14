import json
from plotly.graph_objs import Layout, Figure
from plotly import offline


fname = "lesson7/chapter16/rdb_4.5_month.json"

with open(fname) as f:
    all_data = json.load(f)

eqs = all_data["features"]

mags = []
lons = []
lats = []
hovers = []

for eq in eqs:
    mag = eq["properties"]["mag"]
    mags.append(mag)
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    lons.append(lon)
    lats.append(lat)
    hover = eq["properties"]["title"]
    hovers.append(hover)

data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "marker": {
        "size": [3 * mag for mag in mags],
        "color": mags,
        "colorscale": "Turbo",
        "colorbar": {"title": "Magnitude"},
    },
    "text": hovers
}]
layout = Layout(title="Global Earthquakes 4.5+ Magnitude 30 Days")

fig = {"data": data, "layout": layout}

# fig = Figure(data=data, layout=layout)
# fig.show()

offline.plot(fig, filename="lesson7/chapter16/eq_geoplot.html")
