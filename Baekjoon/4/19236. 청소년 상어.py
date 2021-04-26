from collections import defaultdict
def solve():
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, -1, -1, -1, 0, 1, 1, 1]
    maps = [list(map(int, input().split())) for i in range(4)]
    fish_location = defaultdict(list)
    fish, direction = [], []
    for r in range(4):
        fish.append([maps[r][c] for c in range(0, 8, 2)])
        direction.append([maps[r][c] - 1 for c in range(1, 8, 2)])

    def find(arr, x):
        for r in range(4):
            for c in range(4):
                if arr[r][c] == x:
                    return (r, c)
        return None

    def move(arr, direction, sr, sc):
        for i in range(1, 17):
            coord = find(arr, i)
            if coord == None:
                continue
            r, c = coord
            d = direction[r][c]
            for _ in range(7):
                tr, tc = r + dr[d], c + dc[d]
                if 0 <= tr < 4 and 0 <= tc < 4 and [tr, tc] != [sr, sc]:
                    break
                d = (d + 1) % 8

            arr[r][c], arr[tr][tc] = arr[tr][tc], arr[r][c]
            direction[r][c], direction[tr][tc] = direction[tr][tc], d


    def dfs(arr, direction, r, c, score):
        global ans
        #1. 잡아먹기
        arr = [x[:] for x in arr]
        direction = [x[:] for x in direction]
        score += arr[r][c]
        arr[r][c] = 0
        ans = max(score, ans)

        #2. 이동하기
        move(arr, direction, r, c)

        #3. 상어 움직이기
        rr, rc = dr[direction[r][c]], dc[direction[r][c]]
        while 0 <= r + rr < 4 and 0 <= c + rc < 4:
            if arr[r + rr][c + rc] > 0:
                dfs(arr, direction, r + rr, c + rc, score)
            r += rr
            c += rc
        return

    dfs(fish, direction, 0, 0, 0)



ans = 0
solve()
print(ans)