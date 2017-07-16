"""
Given an array of integers and a number
Check if there are 2 elements in the array that add up to that number
The programm should be running in O(n)
"""

def has_pair_with_sum_in_list(l, s):
    required_values = {}
    for v in l:
        if required_values.get(v, False):
            return True
        else:
            required_values[s-v] = True
    
    return False


l = [2, -3, 5, 1, 3, 7]
s1 = 11
s2 = 10
s3 = 0
print(has_pair_with_sum_in_list(l, s1))
print(has_pair_with_sum_in_list(l, s2))
print(has_pair_with_sum_in_list(l, s3))