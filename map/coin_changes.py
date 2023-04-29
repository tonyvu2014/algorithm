# If I give you coins of denominations {3, 7, 9} (a coin worth 3 cents, a coin worth 7 cents, 
# etc.), can you tell me the minimum number of coins that are needed to make a total of 37? 
# You can assume that an infinite supply of all these coins are available to you.


# Dynamic programming
# Given coins = [c1, c2,...,cN]
# Recursion coin_changes(amount) = min(1 + coin_changes(amount-ci)) for i = [1, N] and coin_changes(amount-ci) >= 0
# Use Dynamic Programming to compute the result bottom up from 1 to amount
# Time complexity O(N*amount)
# Space Complexity O(amount)
def coin_change(coins,  amount):
    if len(coins) == 0:
        return -1

    coin_change_result = [-1 for _ in range(amount+1)]
    coin_change_result[0] = 0

    for a in range(1,  amount+1):
        for c in coins:
            if a - c < 0:
                continue
            if coin_change_result[a - c] == -1:
                continue
            count = 1 + coin_change_result[a - c]
            if coin_change_result[a] == -1:
                coin_change_result[a] = count
            elif count < coin_change_result[a]:
                coin_change_result[a] = count
    
    return coin_change_result[amount]

    
if __name__ == '__main__':
    print(coin_change([3, 5], 7))




