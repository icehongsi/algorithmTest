import heapq
def solution():
    n, m = map(int, input().split())
    maze = [list(input()) for _ in range(n)]
    cost = [[float("inf")] * m for _ in range(n)]; cost[0][0] = 0
    heap = [[0, 0, 0]] #cost, row, col

    def ispath(r, c, price):
        if 0 <= r < n and 0 <= c < m and maze[r][c] == "1": # when path exists:
            if price + 1 < cost[r][c]:
                cost[r][c] = price + 1
                heapq.heappush(heap, [price+1, r, c])


    while heap:
        price, r, c = heapq.heappop(heap)
        ispath(r+1, c, price)
        ispath(r-1, c, price)
        ispath(r, c+1, price)
        ispath(r, c-1, price)

    return cost[-1][-1] + 1






print(solution())