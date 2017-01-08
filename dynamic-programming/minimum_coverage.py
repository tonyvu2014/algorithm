# Given an integer list of size n
# Find the minimum number of consecutive elements in the array that
# contain all the values of that array


def find_minimum_coverage(numbers):
    n = len(numbers);
    
    s = set(numbers)
    value_count = len(s)
    
    coverage_dict = {
        (i,i):  set([numbers[i]]) for i in range(n)   
    }
    
    min_coverage = n;
    
    for i in range(n-1):
        for j in range(i+1, n):
            coverage_dict.update({
                (i, j): set(coverage_dict[(i, j-1)])
            })
            coverage_dict[(i, j)].add(numbers[j])
            if len(coverage_dict[(i, j)]) == value_count and j-i+1 < min_coverage:
                min_coverage = j-i+1 
            
    return min_coverage
    
    
if __name__=='__main__':
    print find_minimum_coverage([1, 3, 0, 7, 4, 3, 5, 4, 1, 9, 7])    
    
