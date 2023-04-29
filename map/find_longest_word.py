# Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

# Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

# Note: D can appear in any format (list, hash table, prefix tree, etc.

# For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

# The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
# The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
# The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.


# check word is a subsequence word by greedy algorithm
# For each letter in the word from left to right, find it in the sequence from the current position
# If found, mark it as the current position, if not found, return False
# We can speed up the search by pre-processing the sequence to create a map from each letter to
# its list of positions in the sequence
# Time complexity: O(N + M*N) where N = length of the sequence, M = number of words
def get_letter_position_map(sequence):
    letter_positions = {}

    # pre-processing, create a map from letters in the sequence
    # to the list of its positions
    for index, letter in enumerate(list(sequence)):
        if letter not in letter_positions:
            letter_positions.update({letter: [index]})
        else:
            letter_positions[letter].append(index)
    
    return letter_positions

def is_word_subsequence(letter_positions, word):
    current_position = -1
    for c in list(word):
        if c not in letter_positions:
            return False
        found = False
        positions = letter_positions[c]
        for p in positions:
            if p <= current_position:
                continue
            else:
                current_position = p
                found = True
                break
        if not found:
            return False

    return True


def find_longest_word(sequence, words):
    letter_positions = get_letter_position_map(sequence)
    print(letter_positions)
    max_len = -1
    longest_word = None
    for word in words:
        if is_word_subsequence(letter_positions, word) and len(word) > max_len:
            max_len = len(word)
            longest_word= word
    return longest_word

if __name__ == '__main__':
    longest_word = find_longest_word('abppplee', ["able", "ale", "apple", "bale", "kangaroo"])
    if not longest_word:
        print('No word found')
    else:
        print('Longest subsequence word: ' + longest_word)


    

