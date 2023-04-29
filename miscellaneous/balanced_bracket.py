# Given a string containing only opening and closing brackets, verify if the the brackets are balanced
# A balanced bracket string means all opening brackets will have closing brackets and vice-versa

# Questions:
# - What is the maximum length of the string
# - Can the input contain anything else rather then opening and closing brackets?
# - What is the expected output? What should I print out?
# - Can the input be empty?

# Given a string
# Return true if the string has balanced brackets, false otherwise
# Time complexity = O(n) where n = length of the string
def check_balanced_brackets(input): # 
    unclosed_bracket_count = 0 # 
    for c in input:
        if c == '[':
            unclosed_bracket_count += 1
        elif c == ']':
            unclosed_bracket_count -= 1
        if unclosed_bracket_count < 0:
            return False

    return unclosed_bracket_count == 0

if __name__ == '__main__':
    print(check_balanced_brackets('][][]'))


