"""
Given an array of size n and an integer k
Find the minimum sum of k consecutive numbers from the array
"""

def get_first_k_sum(a, k):
    s = 0
    for i in range(k):
        s += a[i]

    return s
    

def find_min_of_k_sum(a, k):
    if k > len(a):
        raise ValueError("Invalid input")

    k_sum = get_first_k_sum(a, k)
    min_k_sum = k_sum

    for i in range(1, len(a)-k+1):
        k_sum = k_sum - a[i-1] + a[i+k-1]
        if k_sum < min_k_sum:
            min_k_sum = k_sum
     
    return min_k_sum


a = [12, 4, 5, -6, 10, 7, -3, 8]
k = 4

print(find_min_of_k_sum(a, k))

