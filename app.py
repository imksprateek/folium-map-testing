from flask import Flask, render_template_string
import folium

# create a flask application
app = Flask(__name__)

@app.route("/")
def home():
    lat = 13.1155
    lon = 77.6070
    """Create a map object"""
    mapObj = folium.Map(location=[lat, lon],
                        zoom_start=14)

    # add a marker to the map object
    folium.Marker([lat, lon],
                  popup="<i>This a marker</i>").add_to(mapObj)

    # set iframe width and height
    mapObj.get_root().width = "100%"
    mapObj.get_root().height = "1500px"

    # derive the iframe content to be rendered in the HTML body
    iframe = mapObj.get_root()._repr_html_()

    # return a web page with folium map components embeded in it. You can also use render_template.
    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head>
                <style>
                body{
                    object-fit: fill;
                }
                </style>
                </head>
                <body>
                    <!--<h1>Using iframe to render folium map in HTML page</h1>-->
                    {{ iframe|safe }}
                    <!--<h3>This map is place in an iframe of the page!</h3>-->
                </body>
            </html>
        """,
        iframe=iframe,
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50100, debug=True)
