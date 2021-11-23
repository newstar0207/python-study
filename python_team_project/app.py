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
    duration = int(request.form["duration"])
    
    geocoding  = Geocoding(orig, dest)
    origin_geocoding, destination_geocoding = geocoding.geocoding()

    generateMap = GeneratorMap(origin_geocoding, destination_geocoding)
    findPath = FindPath(
        generateMap.G, generateMap.orig, generateMap.dest, duration
    )

    if duration < 10:
        flash("최소 20분 입니다.")
    else:
        try:
            all_route, all_length = findPath.generate_path()
            folium_map = generateMap.f_map_marker(all_route)
            result_hms = findPath.hms(all_length * 0.9)
            
            return render_template("map.html", folium_map=folium_map, result_hms = result_hms, orig = geocoding.orig, dest = geocoding.dest, duration = duration, all_route = all_route )
        except Exception as error:
            flash("error occured : " + repr(error))
    return render_template("home.html")


@app.route('/learning',  methods=["POST"])
def learning() :
    params = request.get_json()
    # flash(params)
    orig = params['orig']
    dest = params['dest']
    duration = int(params['duration'])
    all_route = list(params['all_route'])
    # print(all_route)
    
    # 학습!!!
    
    return {}
    

if __name__ == "__main__":
    app.run(debug=True)
