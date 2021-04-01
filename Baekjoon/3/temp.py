def dfs(rr, rc, br, bc, count = 0):
    global answer
    if (rr, rc) == (gr, gc) and (br, bc) != (gr, gc) or count > 10:
        answer = min(answer, count)
        return

    def isMovable(r, c, dr, dc, er, ec):
        if 0 <= r + dr < n and 0 <= c + dc < m and ((r+dr, c+dc) == (er, ec) and maze[er][ec] == "O" or (r+dr, c+dc) != (er, ec)) and maze[r + dr][c + dc] != "#":
            return 1
        return 0

    def move(r, c, dr, dc, er, ec):
        if maze[r][c] == "O":
            return r, c
        if isMovable(r, c, dr, dc, er, ec):  # 범위 안에 있으며 갈 수 있는 경우
            return move(r + dr, c + dc, dr, dc, er, ec)  # 도착지가 아닐 경우에는 계속하여 전진
        # 범위 안에 없을 경우
        return r, c  # 마지막 위치 출력

    for dr, dc in d:
        if isMovable(rr, rc, dr, dc, br, bc) or isMovable(br, bc, dr, dc, rr, rc): #빨간 구슬이 움직일 수 있는 경우
            trr, trc = move(rr, rc, dr, dc, br, bc)
            tbr, tbc = move(br, bc, dr, dc, rr, rc)
            trr, trc = move(rr, rc, dr, dc, tbr, tbc)


            if (tbr, tbc) != (gr, gc):
                dfs(trr, trc, tbr, tbc, count + 1)


n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
br, bc, rr, rc, gr, gc = 0, 0, 0, 0, 0, 0
tbr, tbc, trr, trc = br, bc, rr, rc
d = [(1,0), (-1,0), (0, 1), (0, -1)]
answer = 11
# 1. 각 중요 포인트 찾기
for r in range(len(maze)):
    if "R" in maze[r]:
        rr, rc = r, maze[r].index("R")
        maze[rr][rc] = "."
    if "B" in maze[r]:
        br, bc = r, maze[r].index("B")
        maze[br][bc] = "."
    if "O" in maze[r]:
        gr, gc = r, maze[r].index("O")

dfs(rr, rc, br, bc)
if answer == 11:
    print(-1)
else:
    print(answer)
