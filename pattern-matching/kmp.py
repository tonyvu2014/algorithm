"""
KMP algorithm to find the index of the first substring in a string that matches a pattern
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


def find_match(target, pattern):
    n = len(target)
    m = len(pattern)
    if m > n:
        return -1

    target_index = 0
    pattern_index = 0
    partial_match = build_partial_match_table(pattern)
    while target_index + m <= n:
        if target[target_index + pattern_index] == pattern[pattern_index]:
            pattern_index += 1
            if pattern_index == m:
                return target_index
        else:
            if pattern_index == 0:
                target_index += 1
                pattern_index = 0
            else:
                target_index += pattern_index - partial_match[pattern_index-1] 
                pattern_index = partial_match[pattern_index]
    
    return -1


if __name__ == '__main__':
    print(find_match('abcdabebd', 'abe'))
    print(find_match('andgefssdauhd', 'ss'))


