from collections import deque
def solution(board):
    n, answer = len(board), 0
    # 동: 0, 서: 1, 남: 2, 북: 3
    isValidCoordinate = lambda r, c: 1 if 0 <= r < n and 0 <= c < n and board[r][c] != 1 else 0 # 유효 좌표인지 확인하는 함수
    calculateCost = lambda prev, curr: 600 if prev != curr else 100 # 건설 비용을 return하는 함수
    q = deque([])
    costs = [[float("inf")] * n for _ in range(n)]; costs[0][0] = 0 # 소요 비용을 우선 무한대로 설정
    # 아래의 두 좌표는 방향 전환에 대한 비용이 발생하지 않으므로 따로 확인한다.
    # (1, 0), (0, 1) 둘 중 하나에 벽이 있을 수 있으므로 개별적으로 확인해야 할 필요가 있다.
    if isValidCoordinate(1, 0):
        costs[1][0] = 100
        q.append((100, 2, 1, 0))
    if isValidCoordinate(0, 1):
        costs[0][1] = 100
        q.append((100, 0, 0, 1))
    direction = {0: (0, 1), 1: (0, -1), 2: (1, 0), 3: (-1, 0)}

    while q: # q의 원소는 좌표, 그리고 해당 좌표까지 도달하는데 드는 비용 (costs에 저장되어 있는 비용보다 높거나 낮을 수 있음)
        cost, d, r, c = q.popleft()
        costs[r][c] = min(costs[r][c], cost)
        for i in range(4):
            dr, dc = direction[i] # 동서남북에 대해 순회 실시
            if isValidCoordinate(r + dr, c + dc):
                if costs[r + dr][c + dc] >= cost + calculateCost(d, i): # 새로 찾은 비용이 더 저렴할 경우
                    costs[r + dr][c + dc] = cost + calculateCost(d, i) # 교체
                    q.append((cost + calculateCost(d, i), i, r + dr, c + dc)) # q에 추가.

    return costs[-1][-1] # 이 원소가 곧 처음부터 도착지까지 가는데 소요되는 최저 비용이라고 할 수 있다

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
'''
from collections import deque
def solution(board):
    n, answer = len(board), 0
    # 동: 0, 서: 1, 남: 2, 북: 3
    isValidCoordinate = lambda r, c: 1 if 0 <= r < n and 0 <= c < n and board[r][c] != 1 else 0
    calculateCost = lambda prev, curr: 600 if prev != curr else 100
    q = deque([])
    costs = [[float("inf")] * n for _ in range(n)]; costs[0][0] = 0

    if isValidCoordinate(1, 0):
        costs[1][0] = 100
        q.append([2, 1, 0])
    if isValidCoordinate(0, 1):
        costs[0][1] = 100
        q.append([0, 0, 1])
    direction = {0: (0, 1), 1: (0, -1), 2: (1, 0), 3: (-1, 0)}
    while q:
        d, r, c = q.popleft()
        if not isValidCoordinate(r, c):
            continue
        for i in range(4):
            dr, dc = direction[i]
            if isValidCoordinate(r + dr, c + dc):
                if costs[r + dr][c + dc] >= costs[r][c] + calculateCost(d, i):
                    costs[r + dr][c + dc] = costs[r][c] + calculateCost(d, i)
                    q.append((i, r + dr, c + dc))

    return costs[-1][-1]
'''