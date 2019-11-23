from typing import List

def change(amount: int, coins: List[int]) -> int:
    """ This takes into account that the list is sorted """
    if not coins or len(coins) == 0: return 0 if amount else 1
    if len(coins) == 1 and coins[0] > amount: return 0 if amount > 0 else 1
    if len(coins) == 1 and coins[0] == amount: return 1
    if not amount: return 1
    ways = [0 for i in range(0, amount+1)]
    ways[0] = 1
    for coin in coins:
        for a in range(1, amount+1):
            if coin <= a:
                ways[a] = ways[a] + ways[a-coin]

    return ways[amount]

change(7, [1,2,4])

