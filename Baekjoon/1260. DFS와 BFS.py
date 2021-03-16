from collections import defaultdict, deque
def solution():
    node, edge, start = map(int, input().split())
    edge_list = defaultdict(list)
    for _ in range(edge):
        key, value = map(int, input().split())
        edge_list[key].append(value)
        edge_list[value].append(key)

    for key in edge_list:
        edge_list[key] = sorted(edge_list[key])

    def dfs(start):
        visited[start] = True
        print_list.append(start)
        for terminal in edge_list[start]:
            if not visited[terminal]: #방문하지 않았을 경우
                dfs(terminal)

    def bfs():
        queue = deque([start]) # queue 초기화
        while queue:
            node = queue.popleft()
            if visited[node]:
                pass # 이미 방문한 노드일 경우 건너뛰기
            else:
                visited[node] = True
                print_list.append(node)
                for terminal in edge_list[node]:
                    if not visited[terminal]: #방문하지 않았을 경우 추가
                        queue.append(terminal)

    visited, print_list = [False] * (node + 1), []
    dfs(start)
    print(" ".join(map(str, print_list)))

    visited, print_list = [False] * (node + 1), []
    bfs()
    print(" ".join(map(str, print_list)))

solution()