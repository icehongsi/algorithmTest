from itertools import combinations
from collections import deque

def solution():
    q, max_safe= deque([]), 0
    wall = []
    numver_of_Wall = 0
    for r in range(n):
        for c in range(m):
            if chamber[r][c] == 0:
                wall.append((r, c))
            elif chamber[r][c] == 1:
                numver_of_Wall += 1

    def isValidCoordinate(r, c):
        if 0 <= r < n and 0 <= c < m and not visited_temp[r][c]:
            return 1
        return 0 #  범위를 벗어나거나, 이미 방문했거나

    def bfs(q):
        count = 0
        while q:
            r, c = q.popleft()
            if not isValidCoordinate(r, c):  # 유효한 좌표가 아닐 경우 건너뛰기
                continue
            count += 1
            visited_temp[r][c] = True
            chamber_temp[r][c] = 2
            for dx, dy in ((1,0), (-1,0), (0, 1), (0, -1)):
                if isValidCoordinate(r + dx, c + dy) and chamber_temp[r + dx][c + dy] == 0:
                    q.append((r+dx, c+dy))
        return count

    for a, b, c in combinations(wall, 3):
        chamber_temp, visited_temp = [x[:] for x in chamber], [x[:] for x in visited]
        chamber_temp[a[0]][a[1]], chamber_temp[b[0]][b[1]], chamber_temp[c[0]][c[1]] = 1, 1, 1
        virus = 0
        for row in range(n): #bfs: 바이러스로 가득 메우기
            for col in range(m):
                if chamber_temp[row][col] == 2 and not visited_temp[row][col]:
                    q.append((row, col))
                    virus += bfs(q)

        max_safe = max(max_safe, (n * m) - numver_of_Wall - virus - 3)

    print(max_safe)

n, m = map(int, input().split())
chamber = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
solution()



