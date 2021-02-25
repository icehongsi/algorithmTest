# 1. 각 섬에 번호 부여
# 2. 각 타일에 대해 무작위 탐색
import sys
sys.setrecursionlimit(1<<31)
def solution():
    global min_val
    maze = [list(map(int, input().split())) for _ in range(int(input()))]
    visited = [[False] * len(maze) for _ in range(len(maze))]
    mark = 1
    min_val = len(maze) ** 2
    def dfs(r, c, mark):
        if r >= len(maze) or c >= len(maze) or r < 0 or c < 0 or visited[r][c]:
            return
        visited[r][c] = True

        if maze[r][c] != 0:
            maze[r][c] = mark
            dfs(r, c+1, mark)
            dfs(r, c-1, mark)
            dfs(r+1, c, mark)
            dfs(r-1, c, mark)


    for r in range(len(maze)):
        for c in range(len(maze)):
            if not visited[r][c] and maze[r][c] != 0:
                dfs(r, c, mark)
                mark += 1



    def dfs2(r, c, island_number, count):
        global min_val
        if r >= len(maze) or c >= len(maze) or r < 0 or c < 0 or count >= min_val:
            return
        if maze[r][c] not in (0, island_number): #다른 섬에 도달
            min_val = count
            return
        elif maze[r][c] == island_number and count != -1:
            return

        dfs2(r + 1, c, island_number, count + 1)
        dfs2(r - 1, c, island_number, count + 1)
        dfs2(r, c + 1, island_number, count + 1)
        dfs2(r, c - 1, island_number, count + 1)

    for r in range(len(maze)):
        for c in range(len(maze)):
            if maze[r][c] != 0:
                dfs2(r, c, maze[r][c], -1)

    print(min_val)

solution()