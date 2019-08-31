# Given a list of words separated by spaces on the first line
# The next lines are the number of comment n followed by n comments
# Each comment has a product_id on the first line and the comment content on the second line
# Print out the product id in descending order of the number of words found in the comments

import re
from sys import stdin
from collections import defaultdict
from operator import itemgetter


def remove_special_characters(word):
    """
    Remove special characters like !, ?, :, ;, . and , from a word
    """
    return re.sub('[!?:;,.]+', '', word)


lowercase_words = set([word.lower() for word in stdin.readline().split()])
n = int(stdin.readline())

hotel_to_word_count_map = defaultdict(int)
for i in range(n):
    hotel_id = int(stdin.readline())
    comment = stdin.readline()
    comment_words = comment.split()
    comment_lowercase_words = [remove_special_characters(w).lower() for w in comment_words]
    valid_comment_lowercase_words = [w for w in comment_lowercase_words if w in lowercase_words]
    hotel_to_word_count_map[hotel_id] += len(valid_comment_lowercase_words)
            
# Sort the map by word_count descending order and then hotel id ascending order
sorted_hotel_to_word_count = sorted(hotel_to_word_count_map.items(), key=lambda x: (x[1], -x[0]), reverse=True)

print(" ".join([str(x[0]) for x in sorted_hotel_to_word_count]))
