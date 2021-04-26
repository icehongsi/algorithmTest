from collections import defaultdict
def solve():
    for r in range(n):
        for c in range(n):
            if maps[r][c] == -1: #blackhole
                endpoint.add((r, c))
            elif 6 <= maps[r][c] <= 10:
                wormhole[maps[r][c]].append((r, c))

    def game(r, c, d, score):
        rr, rc = r, c
        r, c = r + dr[d], c + dc[d]
        global max_score
        wall_flag = True
        wormhole_flag = True
        while True:
            #if (r, c) in endpoint or (r, c) == (rr, rc): #중단점에 도달했을 경우
            if (r, c) in endpoint:
                max_score = max(max_score, score)
                break
            elif not (0 <= r < n and 0 <= c < n) or maps[r][c] == 5: #범위를 벗어날 경우
                d = walls[5][d] #방향 변경
                r, c = r + dr[d], c + dc[d]
                score += 1
                wall_flag = True # 다시 돌아가서 웜홀이나 벽을 마주칠 경우 이를 반영해야 함
                wormhole_flag = True
            elif 6 <= maps[r][c] <= 10 and wormhole_flag: # 웜홀에 도달했을 경우
                (r, c) = wormhole[maps[r][c]][0] if (r,c) == wormhole[maps[r][c]][1] else wormhole[maps[r][c]][1]
                wormhole_flag = False
            elif 1 <= maps[r][c] < 5 and wall_flag: # 벽에 도달했을 경우 + 벽에 위치한 상태에서 벽을 아직 고려하지 않았을 경우
                d = walls[maps[r][c]][d]
                score += 1
                wall_flag = False
            else:
                r, c = r + dr[d], c + dc[d]
                wall_flag = True
                wormhole_flag = True


    for r in range(n):
        for c in range(n):
            if maps[r][c] == 0:
                for d in range(1,5):
                    endpoint.add((r,c))
                    game(r, c, d, 0)
                    endpoint.remove((r,c))

T = int(input())
dc = {1: 1, 2: -1, 3: 0, 4: 0}
dr = {1: 0, 2: 0, 3: 1, 4: -1}
# 1: 동 2: 서 3: 남 4: 북
walls = {
        1: {1: 2, 2: 4, 3: 1, 4: 3},
        2: {1: 2, 2: 3, 3: 4, 4: 1},
        3: {1: 3, 2: 1, 3: 4, 4: 2},
        4: {1: 4, 4: 3, 3: 2, 2: 1},
        5: {1: 2, 2: 1, 3: 4, 4: 3}
}

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    max_score = 0
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    wormhole = defaultdict(list)
    endpoint = set()
    solve()
    print(f"#{test_case} {max_score}")

'''
from collections import defaultdict
def solve():
    for r in range(n):
        for c in range(n):
            if maps[r][c] == -1: #blackhole
                endpoint.add((r, c))
            elif 6 <= maps[r][c] <= 10:
                wormhole[maps[r][c]].append((r, c))

    def game(r, c, d, score):
        rr, rc = r, c
        global max_score
        wall_flag = True
        wormhole_flag = True
        while True:
            if not (0 <= r < n and 0 <= c < n) or maps[r][c] == 5: #범위를 벗어날 경우
                d = walls[5][d] #방향 변경
                r, c = r + dr[d], c + dc[d]
                score += 1
                wall_flag = True # 다시 돌아가서 웜홀이나 벽을 마주칠 경우 이를 반영해야 함
                wormhole_flag = True
            elif 6 <= maps[r][c] <= 10 and wormhole_flag: # 웜홀에 도달했을 경우
                p, q = wormhole[maps[r][c]]
                if (r, c) == p:
                    r, c = q
                else:
                    r, c = p
                wormhole_flag = False
            elif 1 <= maps[r][c] < 5 and wall_flag: # 벽에 도달했을 경우 + 벽에 위치한 상태에서 벽을 아직 고려하지 않았을 경우
                d = walls[maps[r][c]][d]
                score += 1
                wall_flag = False
            else:
                r, c = r + dr[d], c + dc[d]
                wall_flag = True
                wormhole_flag = True
            if (r, c) in endpoint or (r, c) == (rr, rc): #중단점에 도달했을 경우
                print(score)
                max_score = max(max_score, score)
                break


    for r in range(n):
        for c in range(n):
            if maps[r][c] == 0:
                for d in range(1,5):
                    game(r, c, d, 0)

T = int(input())
dc = {1: 1, 2: -1, 3: 0, 4: 0}
dr = {1: 0, 2: 0, 3: 1, 4: -1}
# 1: 동 2: 서 3: 남 4: 북
walls = {
        1: {1: 2, 2: 4, 3: 1, 4: 3},
        2: {1: 2, 2: 3, 3: 4, 4: 1},
        3: {1: 3, 2: 1, 3: 4, 4: 2},
        4: {1: 4, 4: 3, 3: 2, 2: 1},
        5: {1: 2, 2: 1, 3: 4, 4: 3}
}

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    max_score = 0
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    wormhole = defaultdict(list)
    endpoint = set()
    solve()
    print(f"#{test_case} {max_score}")


'''