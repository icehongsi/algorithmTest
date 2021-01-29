import time
import heapq
def solution(board):
    n = len(board)
    costs = [[1<<31 for _ in range(n)] for _ in range(n)] #cost 저장
    costs[0][0] = 0
    heap = [(0, 0, 0, 0)] #cost, r, c, parent


    def alter(r, c, dx, dy, parent, direction):
        if r + dx < 0 or c + dy < 0 or r + dx >= n or c + dy >= n or board[r+dx][c+dy] == 1:
            return False
        additional_cost = lambda parent, direction: 100 if parent in (0, direction) else 600
        if costs[r + dx][c + dy] >= costs[r][c] + additional_cost(parent, direction) + 600: # 더 최단거리일 경우
            return
        print("progree")
        heapq.heappush(heap, [costs[r][c] + additional_cost(parent, direction), r + dx, c + dy])

        if costs[r + dx][c + dy] > costs[r][c] + additional_cost(parent, direction):
            costs[r + dx][c + dy] = costs[r][c] + additional_cost(parent, direction)



    while heap:
        print(heap)
        cost, r, c, parent = heapq.heappop(heap)
        print(cost, r, c)
        for i in costs:
            print(i)

        alter(r, c, 1, 0, parent, 1)
        alter(r, c, -1, 0, parent, 2)
        alter(r, c, 0, 1, parent, 3)
        alter(r, c, 0, -1, parent, 4)

    for i in costs:
        for j in i:
            print(j, end = "\t")
        print()

    print(costs[n-1][n-1])





cost = 1<<63


print(solution([
[0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
[0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
[0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
[1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    ]))