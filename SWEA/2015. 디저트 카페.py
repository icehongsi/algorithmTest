def traverse(r, c, d, s):
    global start_point, answer
    print(r, c, d, id(s))
    r, c = r + dr[d], c + dc[d]
    if (r, c) == start_point: #처음으로 돌아온 경우 + 북동방향으로 진행중인 경우
        answer = max(len(s), answer)
        return
    elif not(0 <= r < N and 0 <= c < N and desert[r][c] not in s): # 방문 가능 범위를 벗어난 경우
        return
    s.add(desert[r][c])
    traverse(r, c, d, s)
    if d < 3: traverse(r, c, d+1, s)
    s.remove(desert[r][c])

def solve():
    global start_point
    for r in range(N):
        for c in range(N):

            start_point = (r, c)
            print(start_point)
            s = set([desert[r][c]])
            traverse(r, c, 0, s)

for i in range(int(input())):
    N = int(input())
    desert = [list(map(int, input().split())) for _ in range(N)]
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]
    answer = -1
    solve()
    print(f"#{i+1} {answer}")
