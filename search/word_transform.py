###
# Given a dictionary of valid words formed only by lowercase alphabetical characters in each line and ends with *.
# A list of pair of valid word separated by space follows in each line and also ends with *. 
# Return the shortest sequence of transformation to transform the first word to the second one. 
# In a valid transformation, a character in the word is replaced by another lowercase alphabetical character.
# sssPrint out 0 if it is not possible to transform the first word to the second word.
#
# Example: 
# Input: 
# dip
# lip
# mad
# map
# maple
# may
# pad
# pip
# pod
# pop
# sap
# sip
# slice
# slick
# spice
# stick
# stock
# *
# spice stock
# may pod
# *
#
# Output can be:
# spice -> slice -> slick -> stick -> stock
# may -> mad -> pad -> pod
#
###

from string import ascii_lowercase


def get_neighbors(dictionary, word):
    neighbors = []
    for i, letter in enumerate(word):
        for ch in ascii_lowercase:
            if ch == letter:
                continue
            new_word = word[:i] + ch + word[i+1:]
            if new_word in dictionary:
                neighbors.append(new_word)    

    return neighbors


def build_sequence(previous_words, first_word, second_word):
    sequence = []
    current_word = second_word
    while current_word:
        sequence = [current_word] + sequence
        current_word = previous_words.get(current_word, None)

    return sequence    

            
def get_sequence(dictionary, pair):
    first_word = pair[0]
    second_word = pair[1]

    if first_word not in dictionary:
        return 0

    if second_word not in dictionary:
        return 0

    if len(first_word) != len(second_word):
        return 0

    previous_words = {first_word: None}
    result = False
    neighbors = {}
    visited_words = {}
    word_queue = [first_word]
    
    while word_queue:
        current_word = word_queue.pop(0)
        visited_words.update({current_word: True})
        if current_word == second_word:
            result = True
            break
        neighbor_words = neighbors.get(current_word, get_neighbors(dictionary, current_word)) 
        for neighbor_word in neighbor_words:
            if not visited_words.get(neighbor_word, False):
                word_queue.append(neighbor_word)
                previous_words.update({neighbor_word: current_word})

    return build_sequence(previous_words, first_word, second_word) if result else [] 


def read_dictionary():
    dictionary = []
    word = input()
    while word != '*':
        dictionary.append(word)
        word = input()

    return dictionary    


def read_word_pair():
    pairs = []
    line = input()
    while line != '*':
        pair = line.split()
        pairs.append((pair[0], pair[1]))
        line = input()
        
    return pairs


def read_and_solve_word_transformation():
    dictionary = read_dictionary()
    pairs = read_word_pair()
    for pair in pairs:
        sequence = get_sequence(dictionary, pair)
        print((' -> ').join(sequence) if sequence else 0)


if __name__=='__main__':
   read_and_solve_word_transformation() 
