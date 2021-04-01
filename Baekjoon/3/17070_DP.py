from collections import deque
def solution():
    n = int(input())
    house = [list(map(int, input().split())) for _ in range(n)]
    prev, curr = [0, 0], [0, 1]  # 초기의 파이프 위치
    q, count = deque([[prev, curr]]), 0