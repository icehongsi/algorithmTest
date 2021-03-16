from collections import deque
def solution():
    row, col = map(int, input().split())
    lake, swan = [], []
    for i in range(row):
        lake.append(list(input()))
        if "L" in lake[-1]:
            swan.append([i, lake[-1].index("L")])

    visited = [[False for _ in range(col)] for _ in range(row)]


    def bfs(r, c, to):
        queue = deque([[r, c]])
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                if 0 <= (r + dx[i]) < row and 0 <= (c + dy[i]) < col and (not visited[r + dx[i]][c + dy[i]]) and lake[r + dx[i]][c + dy[i]] == ".":
                    visited[r + dx[i]][c + dy[i]] = True
                    lake[r + dx[i]][c + dy[i]] = to
                    queue.append([r + dx[i], c + dy[i]])

    lake[swan[0][0]][swan[0][1]] = "A"
    bfs(swan[0][0], swan[0][1], "A")

    lake[swan[1][0]][swan[1][1]] = "B"
    bfs(swan[1][0], swan[1][1], "B")

    visited = [[False for _ in range(col)] for _ in range(row)]
    queue = deque([[swan[0][0], swan[0][1], 0]])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    min_score = 1<<31
    while queue:
        r, c, score = queue.popleft()
        for i in range(4):
            if 0 <= (r + dx[i]) < row and 0 <= (c + dy[i]) < col and (not visited[r + dx[i]][c + dy[i]]):
                visited[r + dx[i]][c + dy[i]] = True
                if lake[r + dx[i]][c + dy[i]] == "A":
                    queue.append([r + dx[i], c + dy[i], score])
                elif lake[r + dx[i]][c + dy[i]] == "B":
                    min_score = min(score, min_score+1)
                elif lake[r + dx[i]][c + dy[i]] == "X":
                    queue.append([r + dx[i], c + dy[i], score+1])



    print(min_score // 2 + 1)

solution()