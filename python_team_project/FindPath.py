from flask.helpers import flash
import networkx as nx
import osmnx as ox
import random
import folium


class FindPath:
    def __init__(self, graph, orig, dest, time):
        self.G = graph
        self.origin_node = ox.distance.nearest_nodes(graph, orig[1], orig[0])
        self.destination_node = ox.distance.nearest_nodes(graph, dest[1], dest[0])
        self.time = time
        self.orig =orig

    def generate_path(self):
        # edges = ox.graph_to_gdfs(self.G, nodes=False)

        is_not_complete = True
        all_time = 1

        while is_not_complete:

            f_map = folium.Map(self.orig, width="100%", height="100%")
            all_length = 0
            all_route = []
            random_num = random.randrange(1, 3)
            random_node = []

            G_list = list(self.G.nodes)
            G_list_len = len(G_list)

            for i in range(random_num):
                push_random = random.randrange(1, G_list_len)
                random_node.append(G_list[push_random])

            random_node.insert(0, self.origin_node)
            random_node.append(self.destination_node)

            for i in range(len(random_node) - 1):
                route = ox.shortest_path(self.G, random_node[i], random_node[i + 1], weight="length")
                f_map = ox.folium.plot_route_folium(self.G, route, f_map)
                all_route.extend(route)
                route_length = int(
                    sum(ox.utils_graph.get_route_edge_attributes(self.G, route, "length"))
                )
                all_length += route_length

            d_node = {}
            d_node.clear()

            for i in all_route:
                d_node[i] = 0

            for i in all_route:
                d_node[i] = 1 if d_node[i] == 0 else d_node[i] + 1

            check_count = 0

            for i in d_node.values():
                check_count += 1
                if i > 2:
                    all_time += 1
                    break
                if check_count == len(d_node.values()) - 2:
                    is_not_complete = False
        return f_map, all_length
