# A “word square” is an ordered sequence of K different words of length K that, when written one word per line, reads the same horizontally and vertically. For example:


# In this exercise you're going to create a way to find word squares.
# First, design a way to return true if a given sequence of words is a word square.
# Second, given an arbitrary list of words, return all the possible word squares it contains. Reordering is allowed.
# For example, the input list
# [AREA, BALL, DEAR, LADY, LEAD, YARD]


# should output
# [(BALL, AREA, LEAD, LADY), (LADY, AREA, DEAR, YARD)]
# Finishing the first task should help you accomplish the second task.


  
# Brute-Force Solution: O(K^2)

# Better Solution: matrix[i][j] = matrix[j][i] for i = 0 -> K-1, j = i+1 -> K-1 
# Time Complexity O(K^2)

from itertools import permutations


def check_word_square(sequence):
    K = len(sequence)
    if K == 0:
        return False
    letters = []
	# Create a matrix of letter
    for word in sequence:
        if len(word) != K:
            return False
        characters = list(word)
        letters.append(characters) 
    
    for i in range(K):
        for j in range(i+1, K):
            if letters[i][j] != letters[j][i]:
                return False
    return True
	 
                         
def find_word_squares_with_word(word_list, word):
    N = len(word)
    word_list_same_length = list(filter(lambda x: len(x) == N, word_list))
    perms = permutations(word_list_same_length, N-1)
    possible_word_squares = []
    for permutation in list(perms):
            p = list(permutation)
            for i in range(N):
                possible_word_square = p[:]
                possible_word_square.insert(i, word)
                possible_word_squares.append(possible_word_square)
    result = []
    for possible_word_square in possible_word_squares:
        if check_word_square(possible_word_square):
            result.append(possible_word_square)
    return result
		
def find_word_squares(words):
    K = len(words)
    if K == 1:
        return [[words[0]]] if len(words[0]) == 1 else []
    prefix_words = words[:K-1]
    word_squares = find_word_squares(prefix_words)
    word_squares.extend(find_word_squares_with_word(prefix_words, words[K-1]))

    return word_squares

if __name__ == '__main__':
    result = find_word_squares(['AREA', 'BALL', 'DEAR', 'LADY', 'LEAD', 'YARD'])
    print(result)
    # print(check_word_square(['BALL', 'AREA', 'LEAD', 'LADY']))


	
