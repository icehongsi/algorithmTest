from collections import deque
def solve():
    global min_value

    n, w, h = map(int, input().split())
    walls = [list(map(int, input().split())) for _ in range(h)]
    result = []
    def dfs(walls, time):
        global min_value
        if sum(sum(i) for i in walls) == 0:
            min_value = 0
            return
        if time == n:
            count = 0
            for r in range(h):
                for c in range(w):
                    if walls[r][c]:
                        count += 1
            min_value = min(min_value, count)
            return
        isVisited = set()
        for row in range(h): # 최상단에 위치한 곳 구하기
            if len(isVisited) == w:
                break
            for col in range(w):
                if col not in isVisited and walls[row][col] != 0: #BFS 실행
                    isVisited.add(col)
                    temp, count = [x[:] for x in walls], 0
                    q = deque([[row, col, walls[row][col]]])
                    while q:
                        r, c, stretch = q.popleft()
                        if temp[r][c] == 0:
                            continue
                        temp[r][c] = 0
                        count += 1
                        # 동서남북으로 횡단하기
                        for i in range(r - stretch + 1, r + stretch):
                            if 0 <= i < h and temp[i][c] >= 1:
                                q.append([i, c, temp[i][c]])
                        for i in range(c - stretch + 1, c + stretch):
                            if 0 <= i < w and temp[r][i] >= 1:
                                q.append([r, i, temp[r][i]])
                    # 마지막으로, 자리 당기기
                    for r in range(h-2, -1, -1):
                        for c in range(w):
                            if temp[r][c] != 0 and temp[r+1][c] == 0:
                                tr = r
                                while tr+1 < h and temp[tr + 1][c] == 0:
                                    temp[tr+1][c], temp[tr][c] = temp[tr][c], temp[tr+1][c]
                                    tr += 1
                    dfs(temp, time + 1)


    dfs(walls, 0)



min_value = float('inf')
solve()
print(min_value)