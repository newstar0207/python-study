import folium
import osmnx as ox


class GeneratorMap:
    def __init__(self, time, origin, destination):

        self.orig = (origin['lat'], origin['lng'])  # 영진전문대
        self.dest = (origin['lat'], destination['lng'])  # 경대
        self.time = time
        self.G = ox.graph_from_point(self.orig, 1500, network_type="walk")

    def f_map_marker(self, f_map):

        folium.Marker( self.orig, 
                      popup=folium.Popup(f"<b>origin</b>", show=True)).add_to(f_map)
        folium.Marker( self.dest, 
                      popup=folium.Popup(f"<b>destination</b>", show=True)).add_to(f_map)

        return f_map._repr_html_()

    def __hms(self, s):
        hours = s // 3600
        s = s - hours * 3600
        mu = s // 60
        ss = s - mu * 60

        return hours, mu, ss
