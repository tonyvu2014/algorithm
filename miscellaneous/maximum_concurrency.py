# Given the number of current customer service staff n on the first line and the number of data set k on the second line. 
# The next k lines are data. Each line contains 2
# point of time in EPOCH format separated by a space. The first number represents the start time and the second number represents 
# the end time of a conversation between a staff and a customer.
# Find out how many more customer service staff the company needs to hire to ensure that every customer is served.
# Example input:
# 1
# 3
# 134400 338743
# 132324 232000
# 249594 383758
#
# In this case, there are at most 2 calls at the same time, so the company needs to hire 1 more staff
#
# Print out 0 if no more staff is required 

from sys import stdin
from collections import defaultdict

def read_data(data_line):
    return data_line.split() 

n = int(stdin.readline())
k = int(stdin.readline())

time_points = []
time_point_map = defaultdict(int)
for i in range(k):
    time_period = read_data(stdin.readline())
    time_point_map[time_period[0]] += 1 
    time_point_map[time_period[1]] -= 1
    time_points.extend(time_period)

time_points.sort()
concurrent_call_count = 0
max_concurrent_call = 0

for time_point in time_points:
    concurrent_call_count += time_point_map[time_point]
    if concurrent_call_count > max_concurrent_call:
        max_concurrent_call = concurrent_call_count
      
if max_concurrent_call <= n:
    print "0"
else:
    print "{}".format(max_concurrent_call-n)    
   
    
    

    
     

