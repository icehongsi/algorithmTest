def solve():
    disappear = {}
    coord = {
        1: (-1, 0), # 상
        2: (1, 0), # 하
        3: (0, -1), # 좌
        4: (0, 1) # 우
    }

    def cross_time(r, c, d, target):
        if d == 1:
            return [r - target, r + target] if target < r else [r + target, 2 * N - 2 - target]
        if d == 2:
            return [] if target > r


    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]
    while