#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):

    # base
    if len(items) == 1:
        if items[0].size > capacity:
            return 0
        else:
            return items[0].value

    temp = items.pop()

    if temp.size > capacity:
        return knapsack_solver(items, capacity)
    else:
        return max(temp.value + knapsack_solver(items, capacity - temp.size), knapsack_solver(items, capacity))


'''
    result = []
    temp = []
    temp.append(items.pop())
    print(temp)
    print(len(items))

    # base
    if len(items) < 1:
        return
    # recursive part
    result.append(temp.extend(knapsack_solver(items, capacity)))
    result.append([].extend(knapsack_solver(items, capacity)))
    print(result)
    return result
'''

if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
