# You are given a single number N. You can perform any of the 2 operations on  N in each move:
# 1: If we take 2 integers a and b where N = axb then we can change N = max(a,b)
# 2: Decrease the value of N by 1
# Determine the minimum number of moves required to reduce the value of N to 0.
import math
import sys


def down_to_zero(N):
    down_to_zero_count = [-1 for i in range(N+1)]
    down_to_zero_count[0] = 0
    down_to_zero_count[1] = 1

    for i in range(2, N+1):
        count = 1 + down_to_zero_count[i-1]
        for f in range(2, int(i**0.5)+1):
            if i % f == 0:
                count = min(count, down_to_zero_count[i // f] + 1)
        down_to_zero_count[i] = count

    return down_to_zero_count[N]


if __name__ == '__main__':
    print('Enter N:')
    N = int(input())
    print(down_to_zero(N))
