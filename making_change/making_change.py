#!/usr/bin/python

import sys


def making_change(amount, denominations, coin=None, cache=None):

    # initialize 2 variables
    if coin is None:  # coin is index for denominations
        coin = len(denominations)-1

# cache for quicker run time
    if cache is None:
        cache = {i: 0 for i in range(amount + 1)}

   # base case for recursive - if amount is reached return true

    if amount < 0 or coin < 0:
        return 0
    elif cache[amount] > 0:
        print(f'RETURNING  amount = {amount}  cache = {cache[amount]}')
        return cache[amount]
    elif amount == 0:
        return 1

    cache[amount] = making_change(amount, denominations, coin-1, cache) + \
        making_change(
            amount - denominations[coin], denominations, coin,  cache)
    print(f'ASSIGNING  amount = {amount}  cache = {cache[amount]}')
    return cache[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
