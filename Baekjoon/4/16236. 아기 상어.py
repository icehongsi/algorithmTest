import time
from collections import deque

def solve():
    ans = 0 # 아기상어가 최대로 머무는 시간
    r, c, size, count = 0, 0, 2, 0
    for p in range(n):
        for q in range(n):
            if maps[p][q] == 9:
                r, c = p, q # 상어 현재 위치 저장
                maps[p][q] = 0

    d = ((-1, 0), (0, -1), (1, 0), (0, 1))

    while True:
        visited = [[-1] * n for _ in range(n)] #거리를 나타내는 배열 초기화
        visited[r][c] = 0
        q, edible = deque([(r, c)]), []

        while q:
            qlen = len(q)
            while qlen:
                row, col = q.popleft()
                for dr, dc in d:
                    tr, tc = row + dr, col + dc
                    if 0 <= tr < n and 0 <= tc < n and visited[tr][tc] == -1:
                        if 0 < maps[tr][tc] < size: #먹을 수 있는 경우
                            visited[tr][tc] = visited[row][col] + 1
                            edible.append((tr, tc))
                        elif 0 <= maps[tr][tc] <= size: # 통과는 가능한 경우
                            visited[tr][tc] = visited[row][col] + 1
                            q.append((tr, tc))
                qlen -= 1
            if edible: break

        if not edible:
            return ans

        r, c = min(edible) # 상어 좌표 변경
        ans += visited[r][c] # 정답에 추가
        maps[r][c] = 0
        count += 1
        if count == size:
            size, count = size + 1, 0

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
print(solve())