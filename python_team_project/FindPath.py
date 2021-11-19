import networkx as nx
import osmnx as ox


class FindPath :
    def __init__(self, graph, orig, dest, time ) :
        self.G = graph
        self.orig_node = ox.distance.nearest_nodes(G, orig[1], orig[0])
        self.dest_node = ox.distance.nearest_nodes(G, dest[1], dest[0])
        self.time = time
    
    def generate_path(self) :
        # 경로 생성
        
        