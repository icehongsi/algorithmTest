n, m, k = map(int, input().split())
maps = [[[] for _ in range(n)] for _ in range(n)]
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    maps[r-1][c-1].append([m, s, d])

def solve():
    global maps
    for i in range(k):
        temp = [[[] for _ in range(n)] for _ in range(n)]
        for r in range(n): # 1. 파이어볼 이동
            for c in range(n):
                if maps[r][c]: #파이어볼이 있을 경우:
                    for m, s, d in maps[r][c]:
                        rr, cc = (r - (dr[d] * s)) % n,  (c - (dc[d] * s)) % n #속력만큼 이동하기
                        temp[rr][cc].append((m, s, d))

        for r in range(n):
            for c in range(n):
                if len(temp[r][c]) > 1:
                    weight, speed, direction = 0, 0, []
                    for m, s, d in temp[r][c]:
                        weight += m
                        speed += s
                        direction.append(d)
                    # 질량 및 속도 계산
                    weight //= 5
                    speed //= len(temp[r][c])
                    if weight == 0:
                        temp[r][c] = []
                        continue

                    if len(tuple(filter(lambda x: x % 2 == 0, direction))) == len(direction) or \
                            len(tuple(filter(lambda x: x % 2 != 0, direction))) == len(direction): #모두 짝수이거나 모두 홀수일 경우
                        direction = [0, 2, 4, 6]
                    else:
                        direction = [1, 3, 5, 7]

                    temp[r][c] = [[weight, speed, direction[i]] for i in range(4)]
        maps = temp

    # 정답 출력
    ans = 0
    for r in range(n):
        for c in range(n):
            if maps[r][c]:
                for m, s, d in maps[r][c]:
                    ans += m
    print(ans)



solve()