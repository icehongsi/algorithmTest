from itertools import product
def solve():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    direction = {
        1: [0],
        2: [0, 2],
        3: [0, 3],
        4: [0, 2, 3],
        5: [0, 1, 2, 3]
    }
    ans = n * m
    cctv = []
    for r in range(n):
        for c in range(m):
            if 0 < maps[r][c] < 6:
                cctv.append((r, c))

    for chance in product(range(4), repeat = len(cctv)): #chance: 움직여야하는 방향
        temp = [x[:] for x in maps] # 임시 map 할당
        for k, v in enumerate(chance): # k: cctv 인덱스, v: 움직이는 정도
            r, c = cctv[k]
            for dir in direction[maps[r][c]]:
                d = (dir + v) % 4 # cctv가 회전해야하는 각도
                tr, tc = r, c
                rr, rc = dr[d], dc[d]
                while 0 <= tr + rr < n and 0 <= tc + rc < m and temp[tr + rr][tc + rc] != 6: # 범위안에 있으며 벽이 아닌 경우
                    tr, tc = tr + rr, tc + rc
                    if temp[tr][tc] == 0:
                        temp[tr][tc] = -1
        count = 0
        for r in range(n):
            for c in range(m):
                if temp[r][c] == 0:
                    count += 1
        ans = min(count, ans)
    print(ans)

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
solve()