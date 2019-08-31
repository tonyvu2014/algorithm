# Read input from stdin. Each line contains 4 integers separated by a space which represent 4 possible edges of a polygon in order.
#
# Count the total number of square, rectangle or others. A square is not considered a rectangle, invalid input and 
# non-rectangle and non-square will be counted as others.
#
# print out the output as follow:
# <square_count> <rectangle_count> <others_count>

from sys import stdin
from collections import defaultdict


def are_all_positive_numbers(edges):
    return all(x > 0 for x in edges)


def is_square(edges):
    return len(edges) == 4 and len(set(edges)) == 1
    

def is_rectangle(edges):
    return len(edges) == 4 and (edges[0] == edges[2] and edges[1] == edges[3])
    
    
shape_type_count = defaultdict(int) 
for line in stdin:
    edges = [int(edge) for edge in line.split()]
    if len(edges) != 4:
        continue
    if not are_all_positive_numbers(edges):
        shape_type_count['others'] += 1
    elif is_square(edges):
        shape_type_count['square'] += 1
    elif is_rectangle(edges):
        shape_type_count['rectangle'] += 1
    else:
        shape_type_count['others'] += 1
        
print(" ".join([str(shape_type_count[shape_type]) for shape_type in ('square', 'rectangle', 'others')]))                   
    
    

    