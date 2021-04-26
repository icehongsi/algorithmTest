def solve():
    row, col, t = map(int, input().split()) # 1. 입력받기
    space = [list(map(int, input().split())) for _ in range(row)]
    air = []
    isvalidcoordinate = lambda r, c: 1 if 0 <= r < row and 0 <= c < col else 0
    for r in range(row):
        for c in range(col):
            if space[r][c] == -1:
                air.append((r, c))
                break
    # 0. 좌표 r, c별 이동해야 할 방향 저장
    move = [[[0, 0] for _ in range(col)] for _ in range(row)]
    for r in (air[0][0], air[1][0]):
        for c in range(1, col-1):
            move[r][c][1] += 1

    for r in (0, row - 1):
        for c in range(1, col):
            move[r][c][1] -= 1

    for r in range(row):
        if r < air[0][0]:
            move[r][0][0] += 1
        if 0 < r <= air[0][0]:
            move[r][col-1][0] -= 1
        if air[1][0] <= r < row - 1:
            move[r][col-1][0] += 1
        if air[1][0] < r:
            move[r][0][0] -= 1

    d = ((1, 0), (-1, 0), (0, 1), (0, -1)) # 남, 북, 동, 서

    for i in range(t):
        temp = [[0] * col for _ in range(row)]
        # 1. 미세먼지 확산
        for r in range(row):
            for c in range(col):
                if space[r][c] > 0:
                    count = 0
                    for dr, dc in d:
                        if isvalidcoordinate(r+dr, c+dc) and space[r + dr][c + dc] != -1: # 유효한 좌표이며 공기청정기가 없을 경우
                            temp[r + dr][c + dc] += space[r][c] // 5
                            count += 1
                    temp[r][c] += int(space[r][c] - ((space[r][c] // 5) * count))
        # 2. 미세먼지 이동
        temp2 = [[0] * col for _ in range(row)]
        for r in range(row):
            for c in range(col):
                if temp[r][c] > 0:
                    dr2, dc2 = move[r][c][0], move[r][c][1]
                    dust = temp[r][c]
                    if isvalidcoordinate(r + dr2, c + dc2) and space[r+dr2][c+dc2] != -1:
                        temp2[r + dr2][c + dc2] = dust
        temp2[air[0][0]][air[0][1]] = -1
        temp2[air[1][0]][air[1][1]] = -1
        space = [x[:] for x in temp2]

    ans = 0
    for r in range(row):
        for c in range(col):
            if space[r][c] > 0:
                ans += space[r][c]
    print(ans)





solve()
