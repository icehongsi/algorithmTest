# 이전에 실패했던 문제
def isvalidcoordinate(r, c):
    if 0 <= r < n and 0 <= c < n and maps[r][c] != 1:
        return 1
    return 0

def solve(d, cr, cc): #direction, curr row, curr col
    global count
    if (cr, cc) == (n-1, n-1):
        count += 1
        return
    if d == 0:
        if 0 <= cc + 1 < n and maps[cr][cc+1] == 0: # 가로
            solve(0, cr, cc + 1)

    elif d == 1:
        if 0 <= cr + 1 < n and maps[cr+1][cc] == 0: # 세로
            solve(1, cr + 1, cc)

    elif d == 2:
        if 0 <= cc + 1 < n and maps[cr][cc+1] == 0: # 가로
            solve(0, cr, cc + 1)
        if 0 <= cr + 1 < n and maps[cr + 1][cc] == 0: # 세로
            solve(1, cr + 1, cc)

    if 0 <= cr + 1 < n and 0 <= cc + 1 < n and maps[cr + 1][cc] + maps[cr][cc+1] + maps[cr+1][cc+1] == 0: #세로:
        solve(2, cr + 1, cc + 1)

n = int(input())
maps = [list(map(int, input().split())) for i in range(n)]
count = 0
solve(0, 0, 1)
print(count)