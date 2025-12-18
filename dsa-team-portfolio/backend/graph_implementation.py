from .graph_detail import Graph
import json

class MetroMap:
    def __init__(self):
        self.graph = Graph()
        self._build_network()

    def _build_network(self):

        with open('dsa-team-portfolio/data/stations.json', 'r') as f:
            data = json.load(f)
            
        lrt1 = data["lrt1"]
        lrt2 = data["lrt2"]
        mrt3 = data["mrt3"]
        interchanges = data["interchanges"]

        for station in lrt1 + lrt2 + mrt3:
            self.graph.add_vertex(station)

        for line in [lrt1, lrt2, mrt3]:
            for i in range(len(line) - 1):
                self.graph.add_edge(line[i], line[i+1])
                self.graph.add_edge(line[i+1], line[i])

        for a, b in interchanges:
            self.graph.add_edge(a, b)            
            self.graph.add_edge(b, a)

    def get_route(self, start, end, method):
        if start not in self.graph.vertices or end not in self.graph.vertices:
            return "Station not found."
        if method == "DFS":
            return self.graph.dfs(start, end)
        return self.graph.bfs(start, end)