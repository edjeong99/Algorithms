#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    result = []
    plays = ['rock', 'paper', 'scissors']

    def rps_helper(m, arr):
       # base
        if m == 0:
            return result.append(arr)

        # recursive
        for play in plays:
            temp = arr[:]
            temp.append(play)
            rps_helper(m-1, temp)

    rps_helper(n, [])
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
