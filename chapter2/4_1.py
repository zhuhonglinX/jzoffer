

def find(lst, target) -> int:
    m, n = len(lst), len(lst[0])
    row, column = 0, n - 1

    while column > 0 and row < m:
        num = lst[row][column]
        if num == target:
            return True
        elif num > target:
            column -= 1
        elif num < target:
            row += 1
    return False
        

if __name__ == "__main__":
    lst = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15],
    ]
    print(find(lst, 29))



"""Note
二维数组（有序）查找元素，考虑从左下角或者右上角元素作为筛选依据，可以直接筛掉一行或者一列。
"""