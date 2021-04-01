# 20210330 재도전
from collections import deque

def isValidCoordinate(r, c):
    if 0 <= r < row and 0 <= c < col:
        return lake[r][c]
    return float('inf')

def solution():
    d = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for r in range(row):
        for c in range(col):
            lake[r][c] = min([isValidCoordinate(r + dr, c + dc) for dr, dc in d]) + 1

    for _ in lake:
        print(_)
row, col = map(int, input().split())
lake, swan = [], []
for i in range(row):
    temp = list(input())
    for j in range(len(temp)):
        if temp[j] == ".":  # 해빙된 공간은 0
            temp[j] = 0
        elif temp[j] == "X":
            temp[j] = float('inf')  # 해빙되지 않은 공간은 무한으로 설정
        elif temp[j] == "L":
            temp[j] = 0
            swan.append([i, j])
    lake.append(temp)



solution()