###
# Given a list of product pair which belongs to the same category like (2, 3), (4, 1), (3, 5),
# (1, 7), (6, 8), return the number of different product category and list each products in each 
# category
###

# Construct a graph of products as nodes and edges between nodes of the same category
# Find all disconnected subgraph of the newly contructed graph using BFS 
# Time complexity

class Graph:
    def __init__(self, size, adjacency_list):
        self.size =  size
        self.adjacency_list = adjacency_list

    def add_edge(self, v1, v2):
        if v1 in self.adjacency_list:
            self.adjacency_list[v1].add(v2)
        else: 
            self.adjacency_list[v1] = { v2 }

        if v2 in self.adjacency_list:
            self.adjacency_list[v2].add(v1)
        else: 
            self.adjacency_list[v2] = { v1 }


# Build the graph from the list of product pairs
# The graph will be represented as adjacency list
def contruct_graph(pairs):
    adjacency_list = {}

    graph = Graph(len(adjacency_list), adjacency_list) 

    for pair in pairs:
        product1 = pair[0]
        product2 = pair[1]
        graph.add_edge(product1, product2)

    return graph

# Find disjoint components of a graph
def find_disjoint_subgraphs(graph):
    adjacency_list = graph.adjacency_list
    node_count = graph.size

    # Get node list 
    nodes = list(adjacency_list.keys())

    if len(nodes) == 0:
        return []
    
    # Initialize a list of product category
    categories = []

    # Mark all nodes as unvisited
    visited = {}
    for node in nodes:
        visited[node] = False

    for node in nodes:
        if visited[node] == False:
            # Create a BFS queue
            queue = []
            queue.append(node)

            # Create a new category
            category = set([])

            while len(queue) > 0:
                v = queue.pop(0)
                category.add(v)
                for neighbor in adjacency_list[v]:
                    if visited[neighbor] == False:
                        queue.append(neighbor)
                visited[v] = True
            
            categories.append(category)
    
    return categories

# print out the list of category's products
def print_category_list(categories):
    for index, category in enumerate(categories):
        print('Category ' + str(index) + ': ' + str(category))

if __name__ == "__main__":
    product_pairs = [(1, 2), (3, 4)]
    product_graph = contruct_graph(product_pairs)
    categories = find_disjoint_subgraphs(product_graph)
    print(f'Number of categories: {len(categories)}')
    print_category_list(categories)





