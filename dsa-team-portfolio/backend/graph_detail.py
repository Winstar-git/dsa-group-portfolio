class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
     
        if vertex not in self.vertices:
            self.vertices[vertex] = []
        else:
            print(f"Vertex '{vertex}' already exists")

    def add_edge(self, source, target):
       
        if source in self.vertices and target in self.vertices:
            self.vertices[source].append(target)
        else:
            print(f"Error: Both vertices must exist before adding an edge")
    
    def remove_vertex(self, vertex):
      
        if vertex in self.vertices:
            self.vertices.pop(vertex)
            # Remove edges pointing to this vertex
            for v in self.vertices:
                if vertex in self.vertices[v]:
                    self.vertices[v].remove(vertex)
        else:
            print(f"Vertex '{vertex}' not found")
    
    def get_neighbors(self, vertex):
       
        return self.vertices.get(vertex)
    
    def get_all_vertices(self):
       
        return list(self.vertices.keys())
    
    def get_all_edges(self):
        edges = []
        for source, targets in self.vertices.items():
            for target in targets:
                edges.append((source, target))
        return edges
    
    def vertex_count(self):
        return len(self.vertices)
    
    def has_vertex(self, vertex):       
        return vertex in self.vertices
    
    def update_vertex(self, old_vertex, new_vertex):
        if old_vertex in self.vertices:
            # Get the edges of old vertex
            edges = self.vertices[old_vertex]
            # Remove old vertex
            del self.vertices[old_vertex]
            # Add new vertex with same edges
            self.vertices[new_vertex] = edges
            
            # Update references in other vertices
            for v in self.vertices:
                if old_vertex in self.vertices[v]:
                    self.vertices[v].remove(old_vertex)
                    self.vertices[v].append(new_vertex)
        else:
            print(f"Vertex '{old_vertex}' not found")
    
    def clear_graph(self):
        
        self.vertices.clear()
    
    def display_graph(self):
      
        print("\n=== Graph Structure ===")
        if not self.vertices:  # Check if dict is empty
            print("Graph is empty")
        else:
            for vertex, neighbors in self.vertices.items():
                print(f"{vertex} -> {neighbors}")
        print("=" * 25)

    def bfs(self, start, end):
        # Breadth-First Search finds the SHORTEST path in an unweighted graph

        if start not in self.vertices or end not in self.vertices:
            return None 

        visited = set() 
        queue = deque([start])
        parent = {start: None}

        visited.add(start)

        while queue:
            current = queue.popleft()

            if current == end:
                break      

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor) 
                    parent[neighbor] = current
                    queue.append(neighbor)

        path = []
        while end is not None:
            path.append(end)
            end = parent.get(end)

        return path[::-1]

    def dfs(self, start, end):
        # Depth-First Search explores as deep as possible before backtracking

        if start not in self.vertices or end not in self.vertices:
            return None

        visited = set()
        stack = [start]
        parent = {start: None}

        while stack:
            current = stack.pop()

            if current == end:
                break

            if current not in visited:
                visited.add(current)

                # Reverse keeps traversal order consistent
                for neighbor in reversed(self.get_neighbors(current)):
                    if neighbor not in visited:
                        parent[neighbor] = current
                        stack.append(neighbor)

        # Reconstruct the path from end to start
        path = []
        while end is not None:
            path.append(end)
            end = parent.get(end)

        return path[::-1]



my_graph = Graph()
my_graph.add_vertex('David')
my_graph.add_vertex('Miriam')
my_graph.add_vertex('Martin')

my_graph.add_edge('David', 'Miriam')
my_graph.add_edge('David', 'Martin')
my_graph.add_edge('Miriam', 'Martin')

print(my_graph.vertices)

# Find shortest path using BFS
bfs_path = my_graph.bfs('David', 'Martin')
print("\nBFS Path (Shortest Path):")
print(bfs_path)

# Find a path using DFS
dfs_path = my_graph.dfs('David', 'Martin')
print("\nDFS Path:")
print(dfs_path)

# Demonstrate dictionary methods
print("\n=== Dictionary Methods Demo ===")

# dict.keys() - Get all vertices
print(f"All vertices: {my_graph.get_all_vertices()}")

# dict.get() - Get neighbors
print(f"David's neighbors: {my_graph.get_neighbors('David')}")

# dict.items() - Get all edges
print(f"All edges: {my_graph.get_all_edges()}")

# len() - Count vertices
print(f"Number of vertices: {my_graph.vertex_count()}")

# 'in' operator - Check if vertex exists
print(f"Has 'David'? {my_graph.has_vertex('David')}")
print(f"Has 'Alice'? {my_graph.has_vertex('Alice')}")

# Display graph
my_graph.display_graph()



# dict.pop() - Remove vertex
print("\nRemoving 'Martin'...")
my_graph.remove_vertex('Martin')
my_graph.display_graph()

# Update vertex name
print("\nUpdating 'David' to 'Dave'...")
my_graph.update_vertex('David', 'Dave')
my_graph.display_graph()

# dict.clear() - Clear all vertices
print("\nClearing graph...")
my_graph.clear_graph()
my_graph.display_graph()