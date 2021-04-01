#Tier: Silver 1
from collections import deque
'''
def solution():
    col, row = map(int, input().split())
    tomatoes = [list(map(int, input().split())) for _ in range(row)]
    date = [[row * col] * col for _ in range(row)]

    def bfs(r, c):
        count = 0
        visited = [[False] * col for _ in range(row)]
        queue = deque([[r, c]])
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if visited[r][c] or tomatoes[r][c] == -1:
                    continue
                visited[r][c] = True
                date[r][c] = min(date[r][c], count)
                dm = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for d in dm:
                    if r + d[0] < 0 or r + d[0] >= row or c + d[1] < 0 or c + d[1] >= col or visited[r + d[0]][c + d[1]]:
                        continue
                    queue.append([r + d[0], c + d[1]])
            count += 1

    for r in range(row):
        for c in range(col):
            if tomatoes[r][c] == 1:
                bfs(r, c) # 익지 않은 토마토를 발견할 때마다 bfs 실행 >> 비효율적

    max_value = 0
    for r in range(row):
        for c in range(col):
            if date[r][c] == row*col:
                if tomatoes[r][c] == -1:
                    date[r][c] = 0
                elif tomatoes[r][c] == 0:
                    print(-1)
                    return
            max_value = max(max_value, date[r][c])

    print(max_value)
    return







solution()
'''



#Tier: Silver 1
from collections import deque

def solution():
    col, row = map(int, input().split())
    tomatoes = [list(map(int, input().split())) for _ in range(row)]
    date = [[row * col] * col for _ in range(row)]
    queue = deque([])
    visited = [[False] * col for _ in range(row)]

    def bfs():
        count = 0
        dm = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if visited[r][c] or tomatoes[r][c] == -1:
                    continue
                visited[r][c] = True
                date[r][c] = min(date[r][c], count)
                for d in dm:
                    if r + d[0] < 0 or r + d[0] >= row or c + d[1] < 0 or c + d[1] >= col or visited[r + d[0]][c + d[1]]:
                        continue
                    queue.append([r + d[0], c + d[1]])
            count += 1

    for r in range(row):
        for c in range(col):
            if tomatoes[r][c] == 1:
                queue.append([r, c])

    bfs()

    max_value = 0
    for r in range(row):
        for c in range(col):
            if date[r][c] == row*col:
                if tomatoes[r][c] == -1:
                    date[r][c] = 0
                elif tomatoes[r][c] == 0:
                    print(-1)
                    return
            max_value = max(max_value, date[r][c])

    print(max_value)
    return







solution()