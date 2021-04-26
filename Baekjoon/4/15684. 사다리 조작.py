def check():
    for c in range(1, n):
        temp = c
        for r in range(n):
            if lines[c][temp] == 1:
                temp += 1
            elif temp > 0 and lines[c][temp-1] == 1:
                temp -= 1



def dfs(idx, count):
    global ans

    for r in range(h):
        for c in range(n-1):
            if lines[r][c]:
                continue
            if c >= 0 and lines[r][c+1]:
                continue
            if c > 0 and lines[r][c-1]:
                continue

            lines[r][c] = 1
            dfs(r + 1, count + 1)
            lines[r][c] = 0


n, m, h = map(int, input().split()) # n: c, m: r
lines = [[0] * n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    lines[a-1][b-1] = 1

ans = float("inf")
dfs(0, 0)
if ans == float("inf"):
    print(-1)
else:
    print(ans)