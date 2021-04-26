from itertools import combinations
from collections import defaultdict

n = int(input())
test_set = set(range(n))
team = [list(map(int, input().split())) for _ in range(n)]
visited = defaultdict(bool)
min_value = float('inf')
for i in combinations(range(n), n//2):
    i = set(i)
    if tuple(test_set - i) in visited:
        continue
    visited[tuple(test_set - i)] = True
    score = [0, 0]
    for r in range(n):
        for c in range(n):
            if r in i and c in i:
                score[0] += team[r][c]
            elif r not in i and c not in i:
                score[1] += team[r][c]
    min_value = min(min_value, abs(score[0] - score[1]))

print(min_value)


