# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".
# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.
# Return the sentence after the replacement.


# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 100
# dictionary[i] consists of only lower-case letters.
# 1 <= sentence.length <= 106
# sentence consists of only lower-case letters and spaces.
# The number of words in sentence is in the range [1, 1000]
# The length of each word in sentence is in the range [1, 1000]
# Every two consecutive words in sentence will be separated by exactly one space.
# sentence does not have leading or trailing spaces.

class Node:
    # value = character stored at the node
	# children = list of children or None for a leaf node
    def __init__(self, value: str, children: list) -> None:
        self.value = value
        self.children = children

    def add_child(self, node) -> None:
        if not self.children:
            self.children = []
        self.children.append(node)

    # Find a child of this node which stores a certain value
	# Return None if not found
    def find_child_by_value(self, value: str):
        if not self.children:
            return None
        for child in self.children:
            if child.value == value:
                return child
        return None


class Trie:
    def __init__(self, root) -> None:
        self.root = root

	# Add a new word to the Trie
    def add_word(self, word: str) -> None:
        current_node: Node = self.root
        current_children = current_node.children
        letters: list[str]= list(word)
        for letter in letters:
            # next_node = Node(‘a’, Node(‘a’, children))
            next_node: Node = current_node.find_child_by_value(letter) 			
            if not current_children or not next_node:
                new_node: Node = Node(letter, None)					
                current_node.add_child(new_node)
                current_node = new_node
            else: 
                current_node = next_node	
			

# Construct the Trie tree from a list of word
def construct_trie(word_list: list) -> Trie: 
    trie = Trie(Node('', None)) 	
    for word in word_list:
        trie.add_word(word)
    return trie

# Get all words starting from a node given a prefix
def get_words_from_node(node: Node, prefix: str, words: list):
    word = prefix + node.value  
    if not node.children:
        words.append(word)
    else:
        for child in node.children:
            get_words_from_node(child, word, words)
			

# Find all words from a Trie starting with a given prefix
def find_words_with_prefix(trie: Trie, prefix: str) -> list:
    current_node: Node = trie.root
    letters: list[str] = list(prefix)
    for letter in letters:
        node: Node = current_node.find_child_by_value(letter)
        if node:
            current_node = node
        else: 
            return []
    words = []
    get_words_from_node(current_node, prefix[:-1], words)

    return words

# Given a list of prefix and a list of words, return shortest replacements for all the words
def get_replacements(dict: list, words: list) ->  dict:
    trie = construct_trie(words)
    replacements: dict[str, str] = {}
    for prefix in dict:
        words = find_words_with_prefix(trie, prefix)
        for word in words:
            if not replacements.get(word) or len(replacements.get(word)) > len(prefix):
                replacements.update({ word: prefix })
    return replacements

def replace_words(dict: list, sentence: str) -> str:
    words  = sentence.split() 	
    replacements = get_replacements(dict, words)
    new_words = map(lambda x: replacements[x] if x in replacements else x, words)
    return ' '.join(new_words)

if __name__ == '__main__':
    dictionary = ["a","b","c"]
    sentence = "aadsfasf absbs bbab cadsfafs"
    print(replace_words(dictionary, sentence))
                        
         
	
	

