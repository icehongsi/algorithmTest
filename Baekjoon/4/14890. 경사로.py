def solve():
    ans = 0
    N, L = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    #1. 행에 대해서 탐색

    for k in range(2):
        visited = [[0] * N for _ in range(N)]
        for r in range(N):
            flag, height = True, maps[r][0]
            for c in range(N):
                if maps[r][c] == height:
                    continue
                if abs(maps[r][c] - height) > 1:
                    flag = False
                    break
                elif maps[r][c] - height == 1:
                    for i in range(c-L, c):
                        if i < 0 or visited[r][i] or maps[r][i] != height:
                            flag = False
                            break
                    if flag:
                        for i in range(c-L, c):
                            visited[r][i] = True
                        height = maps[r][c]
                    else: break
                elif height - maps[r][c] == 1:
                    for i in range(c, c+L):
                        if i >= N or visited[r][i] or maps[r][i] != maps[r][c]:
                            flag = False
                            break
                    if flag:
                        for i in range(c, c+L):
                            visited[r][i] = True
                        height = maps[r][c]
            if flag:
                ans += 1

        if k == 0:
            temp = [x[:] for x in maps]
            for r in range(N):
                for c in range(N):
                    temp[c][N-r-1] = maps[r][c]
            maps = temp
    print(ans)

solve()