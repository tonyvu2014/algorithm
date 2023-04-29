# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Brute-force: iterate over all the elements the array 4 times, sum them up, if the sum == 
# target, add the 4 elements into the result list
# Time complexity are O(n^4)


# Iterate over the index of the array, compute the sum of all the pairs, store the results in a # # 2-dimention array
# Also remember which 2 elements add up to the certain values in a dictionary
# Iterate again over the 2-dimensional array, compute the remaining after deducted the from # the target. Use the dictionary above, we can find if there are 2 other pairs which add up to # the remaining
# Time complexity O(n^3) 

def is_distinct(list):
	n = len(list)
	unique_n = len(set(list))
	if unique_n < n:
		return False
	return True

def is_new(quadruplets, quadruplet):
    sorted_quadruplet = sorted(quadruplet)
    for q in quadruplets:
        sorted_q = sorted(q)
        if sorted_q == sorted_quadruplet:
            return False
    return True


def find_four_sum_numbers(numbers, target):
    n = len(numbers)
    sum_to_pairs = {}
    quadruplets = []
    for i in range(n-1):
        for j in range(i+1, n):
            total =  numbers[i] + numbers[j]
            remaining = target - total
            if remaining in sum_to_pairs:
                for pair in sum_to_pairs[remaining]:
                    quadruplet = (numbers[i], numbers[j])
                    if not is_distinct([i, j, pair[0], pair[1]]):
                        continue
                    quadruplet += (numbers[pair[0]], numbers[pair[1]])
                    if is_new(quadruplets, quadruplet):
                        quadruplets.append(quadruplet)
            if total in sum_to_pairs:
                sum_to_pairs[total].append((i, j))
            else:
                sum_to_pairs.update({ total: [(i, j)] })

    return quadruplets
	
	
if __name__ == '__main__':
    result = find_four_sum_numbers([1,0,-1,0,-2,2], 0)
    for quadruplet in result:
        print(quadruplet)
