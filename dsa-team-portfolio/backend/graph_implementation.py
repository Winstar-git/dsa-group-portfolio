import json
import os
from .graph_detail import Graph

class MetroMap:
    def __init__(self):
        self.graph = Graph()
        # Dictionary to map station names to their CSS-friendly line class
        self.station_to_line = {}
        self._build_network()

    def _build_network(self):
        # 1. Absolute pathing to prevent 'Internal Server Errors'
        base_path = os.path.dirname(os.path.dirname(__file__))
        data_path = os.path.join(base_path, 'data', 'stations.json')
        
        try:
            with open(data_path, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            # Fallback for different execution environments
            with open('data/stations.json', 'r') as f:
                data = json.load(f)

        # 2. Populate Graph and Line Mapping
        for line_key in ["lrt1", "lrt2", "mrt3"]:
            stations = data[line_key]
            for i in range(len(stations)):
                s = stations[i]
                self.graph.add_vertex(s)
                # Store the line key for CSS class mapping (lrt1, lrt2, mrt3)
                self.station_to_line[s] = line_key
                
                # Connect adjacent stations on the same track
                if i > 0:
                    self.graph.add_edge(stations[i-1], s)

        # 3. Connect Interchange Hubs (Crucial for line-switching)
        # Bridges different line versions of the same station (e.g., Cubao LRT2 to Cubao MRT3)
        for hub_list in data.get("interchanges", []):
            for i in range(len(hub_list)):
                for j in range(i + 1, len(hub_list)):
                    self.graph.add_edge(hub_list[i], hub_list[j])

    def find_route(self, start, end, method="BFS"):
        """
        Calculates the path and returns a list of station objects.
        """
        if method == "BFS":
            raw_path = self.graph.bfs(start, end)
        else:
            raw_path = self.graph.dfs(start, end)

        if not raw_path:
            return None

        # Convert raw string list into a list of dictionaries for the frontend
        # This allows the HTML to use: {{ station.line }} for coloring
        route = []
        for station_name in raw_path:
            route.append({
                "name": station_name,
                "line": self.station_to_line.get(station_name, "mrt3")
            })
        return route