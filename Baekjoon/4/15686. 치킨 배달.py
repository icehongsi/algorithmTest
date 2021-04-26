from itertools import combinations
from collections import defaultdict
def solve():
    ans = float('inf')
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

    # 3. 치킨집간의 거리별로 오름차순 정렬
    for k in distance:
        distance[k].sort(key = lambda x: x[0])
    for i in range(1, m+1):
        for option in tuple(combinations(range(len(chicken)), i)):
            sub_ans = 0
            for dist in distance: #house
                for d in distance[dist]: #house와 각 치킨집별 거리
                    if d[1] in option:
                        sub_ans += d[0]
                        break
            ans = min(sub_ans, ans)
    print(ans)
solve()