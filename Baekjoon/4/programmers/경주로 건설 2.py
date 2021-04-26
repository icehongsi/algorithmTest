from collections import deque


def solution(board):
    n, answer = len(board), 0
    isValidCoordinate = lambda r, c: 1 if 0 <= r < n and 0 <= c < n and board[r][c] != 1 else 0
    calculateCost = lambda prev, curr: 600 if prev != curr else 100
    q = deque([])
    costs = [[float('inf')] * n for _ in range(n)]
    costs[0][0] = 0



    if isValidCoordinate(1, 0):
        costs[1][0] = 100
        q.append((100, 2, 1, 0))
    if isValidCoordinate(0, 1):
        costs[0][1] = 100
        q.append((100, 0, 0, 1))
    direction = {0: (0, 1), 1: (0, -1), 2: (1, 0), 3: (-1, 0)}
    while q:
        cost, d, r, c = q.popleft()
        costs[r][c] = min(costs[r][c], cost)
        for i in range(4):
            dr, dc = direction[i]
            if isValidCoordinate(r + dr, c + dc):
                if costs[r + dr][c + dc] >= cost + calculateCost(d, i):
                    costs[r + dr][c + dc] = cost + calculateCost(d, i)
                    q.append((cost + calculateCost(d, i), i, r + dr, c + dc))
    return costs[-1][-1]

print(solution([[0,0,0],[0,0,0],[0,0,0]]))