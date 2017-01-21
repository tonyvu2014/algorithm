import sys

class Edge(object):
    
    def __init__(self, v1, v2, w = None):
        self.v1 = v1
        self.v2 = v2
        self.w = w
        
    
class Graph(object):
    
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        
    @property    
    def vertex_size(self):
        return len(self.vertices)
        
        
    def adjacent_vertices(self, vertex):
        adjacent_map = {}
        for edge in self.edges:
            if vertex == edge.v1:
                adjacent_map.update({edge.v2: edge.w})
            if vertex == edge.v2:
                adjacent_map.update({edge.v1: edge.w})
                
        return adjacent_map
            
        
def dijsktra(graph, v):
    distance_from_source = initialize_distance(vertices, v)
    visited_set = set([])

    while len(list(visited_set)) < graph.vertex_size: 
        vertex = pick_closest_unvisited_vertex(visited_set, distance_from_source)
        adjacent_vertices = graph.adjacent_vertices(vertex)
        for v in adjacent_vertices:
            if distance_from_source[vertex] + adjacent_vertices[v] < distance_from_source[v]:
                distance_from_source[v] = distance_from_source[vertex] + adjacent_vertices[v]
        visited_set.add(vertex)   
    
    return distance_from_source
    
    
def initialize_distance(vertices, v):
    distance_from_source = {}
    for vertex in vertices:
        distance_from_source.update({
          vertex: sys.maxint  
        })
    distance_from_source[v] = 0
    
    return distance_from_source
    
    
def pick_closest_unvisited_vertex(visited_set, distance_from_source):
    return reduce(lambda x, y: x if distance_from_source[x]<distance_from_source[y] else y, [v for v in distance_from_source if v not in visited_set])
    
    
if __name__ == '__main__':
    vertices = [1,2,3,4,5,6,7,8]
    edges = [
        Edge(1, 2, 5),
        Edge(2, 4, 3),
        Edge(3, 7, 4),
        Edge(4, 6, 8),
        Edge(5, 8, 1),
        Edge(3, 4, 4),
        Edge(8, 3, 2),
        Edge(1, 6, 7),
        Edge(2, 8, 8)
    ]
    
    graph = Graph(vertices, edges)
    distance_from_source = dijsktra(graph, 1)
    
    for v, d in distance_from_source.iteritems():
        print "Shortest distance from {} to 1 is {}".format(v, d)
    
            
    