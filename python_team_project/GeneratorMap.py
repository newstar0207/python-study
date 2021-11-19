import folium
import osmnx as ox

import math


class GeneratorMap:
    def __init__(self, orig, dest, time) -> None:

        self.orig = (35.895622, 128.622427)  # 영진전문대

        self.dest = (35.888851, 128.641663)  # 아양교

        self.time = time

        self.map = folium.Map(self.orig, width="100%", height="100%")

        self.G = ox.graph_from_point(self.orig, 1000, network_type="walk")

    # 1. 노드를 찾음 -> G 주변 노드에서 랜덤의 수의 노드를 가져옴
    # 2. 최단거리 알고리즘으로 길을 생성
    # 3. 길을 이은 후 시간 체크

    def plot_route(self, nodes, actualRouteLength, path):
        # Plot forward and reverse paths in different colours
        routeMap = ox.folium.plot_route_folium(self.G, nodes, self.map)

        # Add marker to start point and show route length as a pop up
        folium.Marker(
            orig=self.orig,
            popup=folium.Popup(
                f"<b>Route length: {math.floor(actualRouteLength)}m</b>", show=True
            ),
        ).add_to(routeMap)
        folium.Marker(
            dest=self.dest,
            popup=folium.Popup(
                f"<b>Route length: {math.floor(actualRouteLength)}m</b>", show=True
            ),
        ).add_to(routeMap)

        return routeMap._repr_html_()
