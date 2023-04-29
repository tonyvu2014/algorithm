# Have the function FindIntersection(strArr) read the array of strings stored in strArr
#  which will contain 2 elements: the first element will represent a list of comma-separated 
# numbers sorted in ascending order, the second element will represent a second list of 
# comma-separated numbers (also sorted). Your goal is to return a comma-separated string 
# containing the numbers that occur in elements of strArr in sorted order. 
# If there is no intersection, return the string false.

# Question: 
# Are all numbers integers or floating points? 
# What are the maximum number of numbers in each element? 
# Will each element contain repeating numbers? 
# Can each of the element be empty? Output is string?

# Brute Force: Split 2 element into 2 array of numbers, create a result as an empty, 
# iterate over each number in the first list, for each of them, 
# iterate over the second list, check if it can be found, 
# if yes, add the element to the result list. 
# Finally convert the result list into a string of numbers separated by comma or 
# return false string if the result list is empty. 
# Time complexity O(n*m) where n, m = lengths of the 2 lists

# Improved Algorithm from the Brute Force: Make use of the information where both arrays are 
# sorted, when searching for an element from the first list in the second list, we can use 
# binary search. Time complexity O(n*logm)

# Better Algorithm: Make full use of the information: both arrays are sorted. 
# When searching for an element from the first list in the second list, we can go from left to right, 
# once found we remember that position. We only need to search from that position 
# in the next iteration for the next element in the first list  
# because we know that all other elements on the left will be smaller than  the element. 
# Time complexity O(n+m) because we iterate over each array only once.



def FindIntersection(strArr):
    if len(strArr) < 2:
        return 'false'
    
    firstList = list(map(lambda x: int(x.strip()), strArr[0].strip().split(','))) if len(strArr[0].strip()) > 0 else []
    secondList = list(map(lambda x: int(x.strip()), strArr[1].strip().split(','))) if len(strArr[1].strip()) > 0 else []

    result = []
    searchIndex = 0
    m = len(secondList)
    for number in firstList:
	    if searchIndex >= m:
		    break
	    for i in range(searchIndex, m):
		    if secondList[i] == number:
			    searchIndex = i+1 
			    result.append(number)
			    break
		    elif secondList[i] > number:
			    searchIndex = i
			    break
    if len(result) == 0:
	    return 'false'
    return ', '. join(list(map(lambda x: str(x), result)))


# Test Cases:
# Case 1: ['1, 2, 4, 7', '2, 3, 7, 8']
# Case 2: ['', '1, 2']
# Case 3: ['1, 4', '2, 3']
# Case 4: ['2,  3', '']

if __name__ == '__main__':
    print(FindIntersection(['2, 3', ' ']))



	


