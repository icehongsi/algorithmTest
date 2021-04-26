def dragonCurve():
    visited = [[0] * 101 for _ in range(101)]
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    ans = 0
    for c, r, d, g in curves: # curve에 대해 for문을 활용해 연산 수행
        curve = [d]
        for i in range(g):
            curve += list(map(lambda x: (x+1) % 4, curve))[::-1]
        visited[r][c] = 1
        for i in curve:
            r, c = r + dr[i], c + dc[i]
            if 0 <= r <= 100 and 0 <= c <= 100:
                visited[r][c] = 1
    for r in range(100):
        for c in range(100):
            if visited[r][c] + visited[r+1][c] + visited[r+1][c+1] + visited[r][c+1] == 4:
                ans += 1

    print(ans)

n = int(input())
curves = [list(map(int, input().split())) for _ in range(n)]
dragonCurve()