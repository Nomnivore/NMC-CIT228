import plotly.graph_objects as go
from plotly import offline

formats = ["PNG", "JPEG", "SVG", "GIF", "Other"]
num_used = [376, 348, 153, 104, 19]

explode = (.175, 0, 0, 0, 0)
wedgeColors = ["#FF3333", "green", "lightblue", "orange", "yellow"]

fig = go.Figure(data=[go.Pie(labels=formats, values=num_used)])

fig.update_traces(
    hoverinfo="label+percent",
    textinfo="label",
    textfont_size=24
)

fig.update_layout(
    title_text="Popular Image Formats on the Web",
    title_font_color="#000011",
    title_font_size=36,
    title_font_family="Courier New",
    title_xref="paper",
    title_yref="paper",
    margin_l=200,
    margin_r=200
)

# fig.show()
offline.plot({"data": fig, "layout": fig.layout}, filename="pie.html")
