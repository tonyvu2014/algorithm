# Given an integer n, count the number of string that can make up from the 5 vowels {a, e, i, o, u} 
# with the following rules:
# - Letter a only can be followed by letter e
# - Letter e can only be followed by letter a or i
# - Letter i cannot be next to another letter i
# - Letter o can only be followed by letter i or u
# - Letter u can only be followed by letter a

# Since the number of permutations can be huge, return the count as modulo division of 9^10 + 7

MODULO_NUMBER = pow(9, 10) + 7

def countPerms(n):
    permsCount = [0 for _ in range(n)]
    permsCount[0] = 5

    endWithLetterPermsCount = [[0 for _ in range(n)] for __ in range(5)]
    for i in range(5):
        endWithLetterPermsCount[i][0] = 1

    for j in range(1, n):
        endWithLetterPermsCount[0][j] = (endWithLetterPermsCount[1][j-1] + endWithLetterPermsCount[2][j-1] + endWithLetterPermsCount[4][j-1]) % MODULO_NUMBER
        endWithLetterPermsCount[1][j] = (endWithLetterPermsCount[0][j-1] + endWithLetterPermsCount[2][j-1]) % MODULO_NUMBER
        endWithLetterPermsCount[2][j] = (endWithLetterPermsCount[1][j-1] + endWithLetterPermsCount[3][j-1]) % MODULO_NUMBER
        endWithLetterPermsCount[3][j] = endWithLetterPermsCount[2][j-1] % MODULO_NUMBER
        endWithLetterPermsCount[4][j] = (endWithLetterPermsCount[2][j-1] + endWithLetterPermsCount[3][j-1]) % MODULO_NUMBER

        permsCount[j] = 0
        for i in range(5):
            permsCount[j] += endWithLetterPermsCount[i][j]
        
    return permsCount[n-1] % MODULO_NUMBER

if __name__ == '__main__':
    print(countPerms(100))


    


