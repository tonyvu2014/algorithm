# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, 
# with one additional edge added. The added edge has two different vertices chosen from 1 to n, 
# and was not an edge that already existed. The graph is represented as an array edges of length n 
# where edges[i] = [ai, bi] indicates that there is an edge between nodes 
# ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
# If there are multiple answers, return the answer that occurs last in the input.


# Questions:
# - What is upper bound for n?
# - What is the format of input? Can I assume it is a list of valid pairs?
# - What should I return? An edge which is a pair of number?


# Brute-Force
# Iterate from right to left the list of edges, remove the edge, keep the remaining edges to form a graph
# Check that graph to see if there is a cycle, if no, return the removed edge
# Use DFS to detect a cycle in the graph
# Time complexity: E * O(N+E) where N = number of vertices, E = number of edges

# Run a DFS from any vertex, keep track of the visiting vertices chain, detect the cycle
# In the cycle, we can remove any edge, so we just need to pick the one that occurs last in the input
# Time Complexity: O(N+E) + O(E) = O(N+2E)

class Graph:
    def __init__(self, n):
        self.n = n # 3
        self.adjacency = { i: [] for i in range(1, n+1) }

    def add_edge(self, u, v):
        self.adjacency[u].append(v)
        self.adjacency[v].append(u)


# Find a cycle in a graph
# Return the list of edges in the cycle if any
# Return [] if no cycle is found
def find_cycle(graph):
    visited = { i: False for i in range(1, graph.n+1) }
    # { 1: True, 2: True, 3: False }
    
    # Keeping track of the visiting vertices
    visiting_list = [] # [1, 2]

    def dfs(graph, v, parent):
        visited[v] = True 
        visiting_list.append(v)

        for u in graph.adjacency[v]:
            if u == parent:
                continue
            elif not visited[u]:
                if dfs(graph, u, v):
                    return True
            else: # detect a cycle
                return True

        visiting_list.pop()
        return False

    source = 1
    if dfs(graph, source, -1):
        return visiting_list
    else:
        return []   

def construct_graph(n, edges):
    graph = Graph(n)
    for u, v in edges:
        graph.add_edge(u, v)
    return graph

def get_edge_index(edges):
    edge_index = {}
    for i, edge in enumerate(edges):
        edge_index.update({
            10*edge[0] + edge[1]: i,
            10*edge[1] + edge[0]: i
        })
    return edge_index

if __name__ == '__main__':
    edges = [[1, 2], [2, 3], [4, 3], [4, 5], [1, 4]]
    graph = construct_graph(5, edges)
    cycle = find_cycle(graph)
    cycle_edges = [[cycle[i], cycle[(i+1) % len(cycle)]] for i in range(len(cycle))]
    edge_index = get_edge_index(edges)
    redundant_edge = None
    index = -1
    for u, v in cycle_edges:
        if edge_index[10*u + v] > index:
            index = edge_index[10*u + v]
    redundant_edge = edges[index]
    print(redundant_edge)



