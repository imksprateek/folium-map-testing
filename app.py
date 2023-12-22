from flask import Flask, render_template_string

# create a flask application
app= Flask(__name__)

@app.route("/")
def home():
    """Create a map object using Leaflet"""
    return render_template_string(
        """
        <!DOCTYPE html>
        <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
                <style>
                    #map {
                        height: 70vh; /* Adjust the percentage as needed */
                        width: 100%;
                        max-width: 3000px;
                        margin: 0 auto;
                    }

                    .leaflet-tooltip-pane, .leaflet-popup-pane {
                        font-size: 16px !important;
                    }

                    .leaflet-marker-icon {
                        width: 30px !important;
                        height: 30px !important;
                    }
                    body{
                    margin:0;
                    padding:0;
                    }
                </style>
            </head>
            <body>
                <h1>Using Leaflet to render a responsive map in HTML page</h1>
                <div id="map"></div>

                <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
                <script>
                    var map = L.map('map').setView([13.1155, 77.6070], 12);

                    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                        attribution: '© OpenStreetMap contributors'
                    }).addTo(map);

                    var marker = L.marker([13.1155, 77.6070]).addTo(map);
                    // No popup binding for the marker
                </script>
            </body>
        </html>
        """
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50100, debug=True)
