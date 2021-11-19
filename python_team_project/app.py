from flask import Flask, render_template, request, flash

import GeneratorMap
import FindPath

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/show_map", methods=["POST"])
def show_map():
    orig = str(request.form["orig"])
    dest = str(request.form["dest"])
    time = int(request.form["time"])

    generateMap = GeneratorMap(orig, dest, time)
    findPath = FindPath(
        generateMap.G, generateMap.orig, generateMap.dest, generateMap.time
    )

    if time < 10:
        flash("최소 20분 입니다.")
    else:
        try:
            time, routePath = FindPath.generate_path()
            folium_map = generateMap.plot_route(time, routePath)
            return render_template("map.html", folium_map=folium_map)
        except Exception as error:
            flash("error occured : " + repr(error))
    return render_template("map.html", orig=orig, dest=dest, time=time)


if __name__ == "__main__":
    app.run(debug=True)
