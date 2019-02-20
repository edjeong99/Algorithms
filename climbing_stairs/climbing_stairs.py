#!/usr/bin/python
# init

import sys


def climbing_stairs(n, cache=None):
    if cache is None:  # if there is no cache, initialize cache as array of 0's
        cache = [0 for i in range(n+1)]

    if n == 0:  # if input is 0, return 1.  this is true only when input is 0
        return 1
    elif n == 1:
        return 1

    elif n == 2:  # if 2 steps left, there are 2 ways to climb
        return 2

    elif n == 3:  # if 3 steps left, there are 4 ways to climb
        return 4

    if cache[n] > 0:  # if there is value in cache index of n, use it
        return cache[n]
    else:
        val = climbing_stairs(
            n - 1, cache) + climbing_stairs(n - 2, cache) + climbing_stairs(n - 3, cache)
        cache[n] = val  # assgin value to cache index of n
        return val


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')


climbing_stairs(3)


'''

'''
