# Given the number of current customer service staff n on the first line and the number of data set k on the second line. 
# The next k lines are data. Each line contains 2 point of time in EPOCH format separated by a space. 
# The first number represents the start time and the second number represents the end time of a conversation between 
# a staff and a customer.
#
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


def read_data_from_line(data_line):
    return data_line.split()


def read_conversation_time_periods(number_of_conversations):
    """
    Read in a list of time periods which have a start time and a end time
    """
    time_periods = []
    for i in range(number_of_conversations):
        time_period = read_data_from_line(stdin.readline())
        time_periods.append([int(t) for t in time_period])
    
    return time_periods


def get_maximum_concurrent_call(time_periods):
    """
    Get the maximum number of concurrent calls given a list of conversation time periods
    """
    time_point_set = set()
    # map from a time point to the count of concurrency at the point, plus 1 for start time, minus 1 for end time
    time_point_concurrent_count_map = defaultdict(int) 
    for time_period in time_periods:
        time_point_concurrent_count_map[time_period[0]] += 1 
        time_point_concurrent_count_map[time_period[1]] -= 1
        time_point_set.update(time_period)

    # sort time points in increasing order
    time_points = sorted(list(time_point_set))

    concurrent_call_count = 0
    max_concurrent_call = 0
    # count the concurrencies at each time point
    for time_point in time_points:
        concurrent_call_count += time_point_concurrent_count_map[time_point]
        if concurrent_call_count > max_concurrent_call:
            max_concurrent_call = concurrent_call_count
    
    return max_concurrent_call


n = int(stdin.readline())
k = int(stdin.readline())
time_periods = read_conversation_time_periods(k)

additional_staff = 0
if n < k:
    max_concurrent_call = get_maximum_concurrent_call(time_periods)
    additional_staff = max_concurrent_call-n if n < max_concurrent_call else 0

print(additional_staff)    
