import collections


def solution():
    computer = int(input())
    path = collections.defaultdict(list)
    for u, v in [list(map(int, input().split())) for _ in range(int(input()))]:
        path[u].append(v)
        path[v].append(u)

    visited = [False] * (computer + 1)

    def dfs(n):
        if visited[n]:
            return
        else:
            visited[n] = True
            for i in path[n]:
                dfs(i)

    dfs(1)
    return sum(visited) - 1




print(solution())