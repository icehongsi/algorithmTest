#collection 모듈 사용 하지 않고 해결
from collections import defaultdict
def solve():
    global ans
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    # 1. 집과 치킨집 좌표 저장
    house, chicken = [], []
    for r in range(n):
        for c in range(n):
            if city[r][c] == 1:
                house.append((r, c))
            elif city[r][c] == 2:
                chicken.append((r, c))

    distance = defaultdict(list)
    # 2. 집에 대해 모든 치킨집과의 거리 저장
    for r, c in house:
        for k, v in enumerate(chicken):
            distance[(r, c)].append((abs(v[0] - r) + abs(v[1] - c), k)) # 0: manhattan distance, 1: 치킨집 번호

    for dist in distance:
        distance[dist].sort(key = lambda x: x[0])
    visited = [False] * len(chicken)
    def dfs(idx, yuji):
        global ans
        if idx < len(chicken):
            if yuji < m:
                visited[idx] = True
                dfs(idx + 1, yuji + 1)
                visited[idx] = False
            dfs(idx + 1, yuji)

        elif idx == len(chicken) and any(visited):
            result = 0
            for dist in distance:
                for d in distance[dist]:
                    if visited[d[1]]:
                        result += d[0]
                        break
            ans = min(ans, result)
            return

    dfs(0, 0)
    print(ans)

ans = float('inf')
solve()