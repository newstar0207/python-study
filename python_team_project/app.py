from flask import Flask, render_template, request, flash
from dotenv import load_dotenv

from GeneratorMap import GeneratorMap
from FindPath import FindPath
from Geocoding import Geocoding


app = Flask(__name__)
load_dotenv()

app.secret_key = "my secret key".encode("utf8")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/show_map", methods=["POST"])
def show_map():
    orig = str(request.form["orig"])
    dest = str(request.form["dest"])
    time = int(request.form["time"])
    
    geocoding  = Geocoding(orig, dest)
    origin_geocoding, destination_geoocoding = geocoding.geocoding()
    

    generateMap = GeneratorMap(time, origin_geocoding, destination_geoocoding)
    findPath = FindPath(
        generateMap.G, generateMap.orig, generateMap.dest, generateMap.time
    )

    if time < 10:
        flash("최소 20분 입니다.")
    else:
        try:
            f_map, all_length = findPath.generate_path()
            folium_map = generateMap.f_map_marker(f_map)
            return render_template("map.html", folium_map=folium_map)
        except Exception as error:
            flash("error occured : " + repr(error))
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
