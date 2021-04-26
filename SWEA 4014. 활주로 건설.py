import time
def solve():
    n, x = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]
    modify = [[False] * n for _ in range(n)]
    ans = 0
    def check(r, c, value):
        if 0 <= r < n and 0 <= c < n and field[r][c] == value and not modify[r][c]:
            modify[r][c] = True
            return True
        return False


    for r in range(n): # 핻을 기준으로 확인
        standard, c, flag = field[r][0], 1, True
        while flag:
            while c < n and field[r][c] == standard: # 기준에 맞을 때까지 c 증가
                c += 1
            if c == n: # 끝까지 문제 없이 도달한 경우
                ans += 1
                break
            elif abs(field[r][c] - standard) > 1: break
            elif standard - field[r][c] == 1: #감소한 경우
                for i in range(c, c+x):
                    if not check(r, i, field[r][c]):
                        flag = False; break
                standard = field[r][c]
                c += x
            elif standard - field[r][c] == -1: #증가한 경우
                for i in range(c-x, c-1):
                    if not check(r, i, field[r][c-1]):
                        flag = False; break
                standard = field[r][c]
    modify = [[False] * n for _ in range(n)]
    for c in range(n):
        standard, r, flag = field[0][c], 1, True
        while flag:
            while r < n and field[r][c] == standard:
                r += 1
            if r == n:
                ans += 1
                break
            elif abs(field[r][c] - standard) > 1: break
            elif standard - field[r][c] == 1: #감소한 경우
                for i in range(r+1, r+x):
                    if not check(i, c, field[r][c]):
                        flag = False; break
                    field[i][c] = field[r][c]
                standard = field[r][c]
                r += x
            elif standard - field[r][c] == -1: #증가한 경우
                for i in range(r-x, r):
                    if not check(i, c, field[r-1][c]):
                        flag = False; break
                standard = field[r][c]

    return ans






print(solve())