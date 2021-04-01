from collections import defaultdict, deque
def solution():
    edges = defaultdict(list)
    node, edge = map(int, input().split())
    for _ in range(edge):
        start, end, weight = map(int, input().split())
        edges[start].append((end, weight))
        edges[end].append((start, weight))

    start, end = map(int, input().split())

    mark = [float("inf") for _ in range(node + 1)]; mark[start] = 0
    queue = deque([start])

    while queue:
        temp = queue.popleft()
        for terminal, value in edges[temp]:
            if mark[terminal] > mark[temp] + value:
                mark[terminal] = mark[temp] + value
                queue.append(terminal)

    return mark[end]


print(solution())