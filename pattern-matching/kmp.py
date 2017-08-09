"""
KMP algorithm to find the first index in a string that matches a pattern
"""

def build_partial_match_table(pattern):
    m = len(pattern)
    partial_match = [0] * m
    for i in range(1, m):
        next_char = pattern[partial_match[i-1]]
        if next_char == pattern[i]:
            partial_match[i] = partial_match[i-1] + 1
        else:
            partial_match[i] = 0

    return partial_match


def get_mismatch(target, pattern, index):
    m = len(pattern)
    for i in range(m):
        if target[index + i] != pattern[i]:
            return i

    return -1

def find_match(target, pattern):
    n = len(target)
    m = len(pattern)
    if m > n:
        return -1

    first_match = target[:m]
    if first_match == pattern:
        return 0

    index = 1
    partial_match = build_partial_match_table(pattern)
    while index + m <= n:
        mismatch_index = get_mismatch(target, pattern, index)
        if mismatch_index == -1:
            return index
        if mismatch_index == 0:
            index = index + 1 
        else:
            index = index + m - partial_match[mismatch_index-1] - 1
    
    return -1


if __name__ == '__main__':
    print(find_match('abcdabebd', 'abe'))
    print(find_match('andgssdauhd', 'ss'))


