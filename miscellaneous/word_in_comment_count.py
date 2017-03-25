# Given a list of words separated by spaces on the first line
# The next line is the number of comment n which is followed by n comments
# Each comment has a product_id on the first line and the comment content on the second line
# Print out the product id in descending order of the number of words found in the comments

from sys import stdin
from collections import defaultdict
from operator import itemgetter

words = set(map(lambda x: x.lower(), stdin.readline().split()))
n = int(stdin.readline())
product_word_count_map = defaultdict(int)
for i in range(n):
    product_id = int(stdin.readline())
    comment = stdin.readline()
    comment_words = comment.split()
    comment_words_lowercase = map(lambda x: x.lower(), comment_words)
    comment_words = filter(lambda w: w in comment_words_lowercase, words)
    product_word_count_map[product_id] += len(comment_words)
            
sorted_product_word_count_map = sorted(product_word_count_map.items(), key=itemgetter(1), reverse=True)
print " ".join([str(x[0]) for x in sorted_product_word_count_map])
