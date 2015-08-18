# -*- coding: utf-8 -*-
# Copyright 2015 IFOOTH
# Author: Joe Lei <thezero12@hotmail.com>


def count_neighbours(grid, row, col):
    # 左边
    row_l, col_l = len(grid), len(grid[0])
    count = 0
    x = [row - 1, row, row + 1]
    y = [col - 1, col, col + 1]
    for i in x:
        if i < 0 or i > row_l - 1:
            continue
        for j in y:
            if j < 0 or j > col_l - 1:
                continue
            if i == row and j == col:
                continue
            if grid[i][j] == 1:
                count += 1
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
