

def solution():
    global current_area
    n = int(input())
    map = [list(input()) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    result = []

    def dfs(r, c):
        global current_area
        if 0 <= r < n and 0 <= c < n and not visited[r][c] and map[r][c] == "1":
            current_area += 1
            visited[r][c] = True
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return True

        return 0

    for r in range(n):
        for c in range(n):
            if dfs(r, c):
                result.append(current_area)
                current_area = 0

    print(len(result))
    for i in sorted(result):
        print(i)

current_area = 0
solution()