# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
# you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. 
# If there are many valid answers, return any of them. 
# If it is impossible to finish all courses, return an empty array.

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

def get_node_indegrees(numCourses, prerequisites):
    indegrees = [0 for _ in range(numCourses)] # [0, 1, 1, 1, 1]
    for p, q in prerequisites:
        indegrees[p] += 1
    return indegrees

def get_course_ordering(numCourses, prerequisites):
    course_dependency_graph = get_prerequisites_graph(numCourses, prerequisites)
    indegrees = get_node_indegrees(numCourses, prerequisites)
    

    # Queue all the nodes with 0 indegree
    queue = []
    for i in range(numCourses):
        if indegrees[i] == 0:
            queue.append(i) 

    # Mark all nodes as unvisted, set visited_count as 0
    visited = [False] * numCourses
    visited_count = 0

    # Initialize an empty visiting_list (will be in order)
    visiting_list = []   

    # Take from the queue if they are not empty
    while len(queue) > 0:
        course = queue.pop(0)
        visiting_list.append(course)
        visited[course] = True
        visited_count += 1  

        # Iterate over all the neighbor courses (courses that have the current course as a prerequisite)
        for v in course_dependency_graph.adjacency[course]:
            if not visited[v]:
                indegrees[v] -= 1 # One incoming node is out, decrease indegree values by 1
                if indegrees[v] == 0: # If in degree = 0, add to the queue to process next
                    queue.append(v)

    # If not all nodes are visited, there must be a cycle
    if visited_count < numCourses:
        return []
    else:
        return visiting_list
    
if __name__ == '__main__':
    course_schedule = get_course_ordering(5, [[0, 1], [2, 3], [4, 1]])
    print(course_schedule)

