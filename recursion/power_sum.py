def count_ways(X, N):
    # Create an empty list to store the ways
    ways = []

    # Define a recursive helper function to find the ways
    def find_ways(current_sum, current_num, current_list):
        # Base case: if the current sum is X, add the current list to the ways
        if current_sum == X:
            ways.append(current_list)
            return

        # If the current sum is greater than X, stop recursing
        if current_sum > X:
            return

        # Recursive case: try all possible next numbers
        current_list_copy = current_list[:]
        for i in range(current_num+1, int(X**(1/N))+1):
            next_sum = current_sum + i**N
            new_current_list = current_list_copy + [i]
            find_ways(next_sum, i, new_current_list)

    # Call the recursive function to find the ways
    find_ways(0, 0, [])

    # Return the number of ways found
    print(ways)
    return len(ways)


if __name__ == '__main__':
    print(count_ways(90, 2))
