# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
# you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. 
# If there are many valid answers, return any of them. 
# If it is impossible to finish all courses, return an empty array.

# Questions:
# - How many courses can it have?
# - Will the course prerequisites always be valid? Will it have cyclic prerequisites? c->b->a->c
# - What is the input format? a list of pair?
# - What should be the format to return? (an array of course numbers?)

class Graph:
    def __init__(self, n):
        self.n = n
        self.adjacency = [[] for _ in range(n)]
        self.has_cycle = False

    def add_edge(self, u, v):
        self.adjacency[u].append(v)


# [ai, bi] = bi -> ai

# Given the prerequisites, return the directed graph of course dependency
def get_prerequisites_graph(numCourses, prerequisites):
    course_dependency_graph = Graph(numCourses)
    for p, q in prerequisites:
        course_dependency_graph.add_edge(q, p)
    return course_dependency_graph

def dfs(graph, u, color, visiting_list):
    color[u] = 'GREY'
    for v in graph.adjacency[u]:
        if color[v] == 'GREY':
            graph.has_cycle = True
            break
        elif color[v] == 'WHITE':
            dfs(graph, v, color, visiting_list)
    color[u] = 'BLACK'
    visiting_list.append(u)

def bfs(graph, u):
    visiting_list = []
    queue = []
    visited = [False] * graph.n

    visited[u] = True
    visiting_list.append(u)
    queue.append(u)

    while len(queue) > 0:
        node = queue.pop(0)
        for v in graph.adjacency[node]:
            if not visited[v]:
                queue.append(v)
        visited[node] = True
        visiting_list.append(node)
    
    return visited, visiting_list


def get_course_ordering(numCourses, prerequisites):
    # construct the course dependency graph from the prerequisites
    # perform a DFS of the graph from any node, keep adding to the course schedule list
    # while keeping track of node which has been visited
    # if the a childless node is reached, move to the next node which has not been visited yet
    course_dependency_graph = get_prerequisites_graph(numCourses, prerequisites)
    stack = []
    color = ['WHITE'] * numCourses
    for i in range(numCourses):
        if color[i] == 'WHITE':
            dfs(course_dependency_graph, i, color, stack)
            if course_dependency_graph.has_cycle:
                print('Course ordering is impossible')
                break
    
    course_schedule = [] if course_dependency_graph.has_cycle else [stack.pop() for _ in range(numCourses)]

    return course_schedule

if __name__ == '__main__':
    course_schedule = get_course_ordering(5, [[1, 0],[2, 3],[4, 1], [3, 0]])
    print(course_schedule)


    