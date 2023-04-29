def reverse_string(input: str) -> str:
    # iterate over all characters in the string from left to right
    # add each character to a stack
    # pop the characters from the stack one by one until the stack is empty
    # add that character to a initially empty string
    # Time complexity: O(n) where n = length of the input string
    letters = list(input)
    q = []
    for letter in letters:
        q.append(letter)
    output = ''
    while q:
        c = q.pop()
        output += c
    return output

if __name__ == '__main__':
    print(reverse_string(''))
    print(reverse_string('abc'))
    print(reverse_string('a'))