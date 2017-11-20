'''
Given an array  of  elements, find the maximum possible sum of a

1.Contiguous subarray
2. Non-contiguous (not necessarily contiguous) subarray.

Empty subarrays/subsequences should not be considered.

Input Format:

First line of the input has an integer .  cases follow. 
Each test case begins with an integer . In the next line,  integers follow representing the elements of array .

Constraints:

The subarray and subsequences you consider should have at least one element.

Output Format:

Two, space separated, integers denoting the maximum contiguous and non-contiguous subarray. At least one integer should be selected and put into the subarrays (this may be required in cases where all elements are negative).

Sample Input:

2 
4 
1 2 3 4
6
2 -1 2 3 4 -5
	
Sample Output:

10 10
10 11
	
Explanation:

In the first case: 
The max sum for both contiguous and non-contiguous elements is the sum of ALL the elements (as they are all positive).

In the second case: 
[2 -1 2 3 4] --> This forms the contiguous sub-array with the maximum sum. 
For the max sum of a not-necessarily-contiguous group of elements, simply add all the positive elements.
'''

import sys

def find_max_subsequences(array):
    x = find_max_contiguous_sum(array)
    y = find_max_non_contiguous_sum(array)
    return (x, y)
    
    
def find_max_subsequences_kadane(array):
    x = find_max_contiguous_sum_kadane(array)
    y = find_max_non_contiguous_sum(array)
    return (x, y)
    
    
def find_max_contiguous_sum(array):
    l = len(array)
    left_indexes = right_indexes = {}
    found = False
    for i in range(l):
        left_indexes.update({i:False})
        right_indexes.update({i:False})        
        if array[i] >= 0 and (i==0 or array[i-1] < 0):
            left_indexes.update({i:True})
            found = True
        if array[i] >=0 and (i==l-1 or array[i+1] < 0):
            right_indexes.update({i:True})     
            found = True   
           
    if not found:
        return max(array)
        
    max_sum = current_sum = -sys.maxint-1
    for i in range(l):
        if left_indexes.get(i, False):
            if current_sum < 0:
                left_index = i
                current_sum = 0
        current_sum += array[i]        
        if right_indexes.get(i, False):
            if current_sum > max_sum:
                max_sum = current_sum
                
    return max_sum
					
					
def find_max_contiguous_sum_kadane(array):
    max_ending_here = max_so_far = array[0]
    for x in array[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far             								             
                       
            
def find_max_non_contiguous_sum(array):
    max_sum = 0
    for a in array:
        if a>=0:
            max_sum += a
    return max_sum or max(array)             


def compute_max_subsequence():
    test_cases = int(input())
    outcomes = []

    for _ in range(test_cases):
        n = int(input())
        line = sys.stdin.readline()
        array = map(lambda x: int(x), line.split(" "))
        outcomes.append(find_max_subsequences(list(array)))
   
    for outcome in outcomes:
        print("{} {}".format(outcome[0], outcome[1]))

def compute_max_subsequence_kadane():
    test_cases = int(input())
    outcomes = []

    for _ in range(test_cases):
        n = int(input())
        line = sys.stdin.readline()
        array = map(lambda x: int(x), line.split(" "))
        outcomes.append(find_max_subsequences_kadane(list(array)))
   
    for outcome in outcomes:
        print("{} {}".format(outcome[0], outcome[1]))
   

if __name__ == '__main__':
    compute_max_subsequence()
    
    # Solution using Kadane's algorithm
    compute_max_subsequence_kadane()    
