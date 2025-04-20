from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:

    return [[i*j for j in range(column_start,column_end+1)] for i in range(row_start, row_end+1)]

"""Input:
row_start = 2
row_end = 4
column_start = 3
column_end = 7

Output: [[6, 8, 10, 12, 14], [9, 12, 15, 18, 21], [12, 16, 20, 24, 28]]
that is equal to the following multiplication table:

    3   4   5   6   7   
2   6   8   10  12  14  
3   9   12  15  18  21  
4   12  16  20  24  28"""

if __name__ == '__main__':
    assert check(2,4,3,7) == [[6, 8, 10, 12, 14], [9, 12, 15, 18, 21], [12, 16, 20, 24, 28]]
