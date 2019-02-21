#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    print(f'size = {len(items)} items = {items[len(items)-1]}')
    # base
    if len(items) == 1:
        #    print(f'LAST ITEM temp = {temp}')
        if items[0].size > capacity:
            return 0
        else:
            return items[0].value

    temp = items.pop()
    #print(f'temp = {temp}')
    if temp.size > capacity:
        print(f'out of size capacity = {capacity}  temp = {temp}')
        return knapsack_solver(items, capacity)
    else:
        print(f'FIT capacity = {capacity}  temp = {temp}')

        return max(temp.value + knapsack_solver(items, capacity - temp.size),
                   knapsack_solver(items, capacity))


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
