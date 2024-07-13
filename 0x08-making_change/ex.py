#!/usr/bin/python3


"""
Step1
check if 
"""

# def makeChange(coins, total):
#     if total == 0 or total < 0:
#         return 0
#     
#     change = findChange(coins, total)
#     return change


def findChange(coins, total):
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    if dp[total] != float('inf'):
        return dp[total]
    else:
        return -1


def makeChange(coins, total):
    if total == 0 or total < 0:
        return 0
    
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    coin_index = 0
    coins_len = len(coins)
    
    while coin_index < coins_len:
        coin = coins[coin_index]
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
        coin_index += 1
    
    return dp[total] if dp[total] != float('inf') else -1
    
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))