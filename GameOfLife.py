# -*- coding: utf-8 -*-

import time
import copy

def main():
    grid = [[0 for i in range(50)] for j in range(50)]

    grid[1][2] = 1
    grid[2][3] = 1
    grid[3][1] = 1
    grid[3][2] = 1
    grid[3][3] = 1

    while True:
        display(grid)
        grid = check(grid)
        time.sleep(0.7)
        print()

def check(arr):
    new = copy.deepcopy(arr)
    for row in range(0, len(arr)):
        for col in range(0, len(arr)):
            n = surr(arr, row, col)

            if n < 2 or n > 3:
                new[row][col] = 0

            if new[row][col] == 0 and n == 3:
                new[row][col] = 1
    return new

def surr(arr, x, y):
    return oob(arr, x-1,  y-1) + oob(arr, x-1, y) + oob(arr, x-1, y+1) + oob(arr, x, y-1) +\
        oob(arr, x, y+1) + oob(arr, x+1, y-1) + oob(arr, x+1, y) + oob(arr, x+1, y+1)

def oob(arr, x, y):
    try:
        if x < 0 or y < 0:
            return 0
        else:
            return arr[x][y]
    except IndexError:
        return 0

def display(arr):
    for i in arr:
        for j in i:
            if j == 0:
                print("□ ", end='')
            else:
                print("■ ", end='')
        print()

if __name__ == "__main__": main()
