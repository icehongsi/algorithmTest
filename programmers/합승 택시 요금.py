import collections
import heapq
def solution(n, s, a, b, fares):
    # n: 지점 개수, s: 출발 지점, a: A 도착지점, b: B 도착지점
    fare_grid = [[float('inf') for _ in range(n)] for _ in range(n)]  # 최대 비용으로 설정
    for u, v, w in fares:
        fare_grid[u - 1][v - 1] = w  # destination, price
        fare_grid[v - 1][u - 1] = w

    for i in range(n):
        fare_grid[i][i] = 0

    print(fare_grid)
    for transf in range(n):  # transfer point
        print(fare_grid)
        for start in range(n):
            for end in range(n):
                fare_grid[start][end] = min(fare_grid[start][end], fare_grid[start][transf] + fare_grid[transf][end])

    # (s -> a) + (a -> b)와 (s -> b) + (b -> a) 중 작은 값 출력

    return min(fare_grid[s-1][i-1] + fare_grid[i-1][a-1] + fare_grid[i-1][b-1] for i in range(n))


'''

def solution(n, s, a, b, fares):
    # n: 지점 개수, s: 출발 지점, a: A 도착지점, b: B 도착지점
    path = collections.defaultdict(list)  # 경로

    for u, v, w in fares:
        path[u - 1].append((v - 1, w))  # destination, fare
        path[v - 1].append((u - 1, w))
    cost = [float('inf')] * (n)
    cost[s - 1] = 0
    parents = [None] * n
    heap = [[0, s-1]]  # cost, node number

    while heap:
        print(cost)
        min_fare, index = heapq.heappop(heap)
        if cost[index] > min_fare:
            continue
        for i in (path[index]):
            if cost[i[0]] > min_fare + i[1]:
                cost[i[0]] = min_fare + i[1]
                heapq.heappush(heap, (cost[i[0]], i[0]))
                parents[i[0]] = index

    # 경로 탐색
    print(parents)
    path_to_a, path_to_b = [], []
    a_parent, b_parent = parents[a - 1], parents[b - 1]
    while a_parent:
        path_to_a.append(parents[a - 1])
        a_parent = parents[parents[a - 1]]
    while b_parent:
        path_to_b.append(parents[b - 1])
        b_parent = parents[parents[b - 1]]

    print(path_to_a, path_to_b, sep = "\n")

    print(cost)


solution(
    6, 4, 6, 2,
    [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
)
