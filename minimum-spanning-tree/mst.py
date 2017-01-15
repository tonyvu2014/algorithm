
class Graph(object):

    def __init__(self):
        self.vertices = set([])
        self.vertex_map = {}
        self.edge_weight = {}
        
    def add_edge(self, edge, weight):
        self.edge_weight.update({
            edge: weight
        })
        self.add_vertex(edge[0])
        self.add_vertex(edge[1])
        self.__update_vertex_map__(edge)
        
    def add_vertex(self, vertex):
        self.vertices.add(vertex)
        if vertex not in self.vertex_map:
            self.vertex_map.update({
                vertex: set([])
            })
        
    def __update_vertex_map__(self, edge): 
        self.vertex_map.get(edge[0]).add(edge[1])
        self.vertex_map.get(edge[1]).add(edge[0])
            
        for v in self.vertex_map:
            if edge[0] in self.vertex_map.get(v) or edge[1] in self.vertex_map.get(v):
                self.vertex_map[v].update(self.vertex_map[edge[1]])
                self.vertex_map[v].update(self.vertex_map[edge[0]])                  
        
    @property    
    def vertex_size(self):
        return len(self.vertices) 
        
    def __str__(self):
        graph_str = ""
        for e, w in self.edge_weight.iteritems():
             graph_str += "{}-{}: {}\n".format(e[0], e[1], w)
        return graph_str    
                     
        
def kruskal(graph):
    sorted_edge_list = sorted([e for e in graph.edge_weight], key=lambda x: graph.edge_weight[x])
    
    mst = Graph()
    for _ in range(graph.vertex_size-1):
        has_cycle = True
        while has_cycle:
            if not sorted_edge_list:
                return None
            edge = sorted_edge_list.pop(0)                
            has_cycle = make_cycle(mst, edge)
        mst.add_edge(edge, graph.edge_weight[edge])
        
    return mst    
    
    
def make_cycle(graph, edge):
    return edge[1] in graph.vertex_map.get(edge[0], set([]))
    
    
def prim(graph):
    sorted_edge_list = sorted([e for e in graph.edge_weight], key=lambda x: graph.edge_weight[x])
    
    mst = Graph()
    mst.add_vertex(next(iter(graph.vertices)))
    while mst.vertex_size < graph.vertex_size:
        found = False
        for edge in sorted_edge_list:
            if len(set(edge).difference(mst.vertices)) == 1:
                found = True
                break
        if found:
            mst.add_edge(edge, graph.edge_weight[edge]) 
        else:
            return None        
        
    return mst           
        
if __name__=='__main__':
    weighted_map = {
        (1,2): 5,
        (2,4): 3,
        (1,5): 7,
        (3,6): 8,
        (4,6): 2,
        (1,6): 4,
        (3,5): 3
    }
    graph = Graph()
    for v, w in weighted_map.iteritems():
        graph.add_edge(v, w)
    print("Initial Graph:")
    print(graph)    
        
    kruskal_mst = kruskal(graph)
    print("Kruskal's Algorithm:")
    print(kruskal_mst)
   
    print("Prim's Algorithm:")
    prim_mst = prim(graph)
    print(prim_mst)
    
    
    
    