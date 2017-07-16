"""
Given a positive number n, return k which is the smallest number in which n can be displayed as 
sum of k perfect square numbers.

For example:

n = 5 => k = 2 (n = 4+1)
n = 7 => k = 4 (n = 4+1+1+1) 

"""
import sys
import math


def get_min_number_of_squares_count(n):
    min_number_of_squares_count = {}
    for i in range(1, n+1):
        if is_perfect_square(i):
            min_number_of_squares_count[i] = 1
        else:
            min_count = sys.maxsize
            for j in range(1, int(i/2)+1):
                current_min_count = min_number_of_squares_count[j] + min_number_of_squares_count[i-j]
                if current_min_count < min_count:
                    min_count = current_min_count

            min_number_of_squares_count[i] = min_count

    return min_number_of_squares_count[n]          


def is_perfect_square(n):
    sqrt_int = int(math.sqrt(n))
    return n == sqrt_int * sqrt_int


for i in range(1, 21):
    print("{}: {}".format(i, get_min_number_of_squares_count(i)))

