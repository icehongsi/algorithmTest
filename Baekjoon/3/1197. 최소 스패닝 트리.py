
def MST():
    included_node = set()
    answer = 0

    for start, end, value in edges:
            if start in included_node and end in included_node:
                continue
            included_node.add(start)
            included_node.add(end)
            answer += value
    print(included_node)
    print(answer)


V, E = map(int, input().split())
#edges = [[float('inf')] * V for _ in range(V)]
edges = [list(map(int, input().split())) for _ in range(V)]
edges = sorted(edges, key = lambda x: x[2])
MST()