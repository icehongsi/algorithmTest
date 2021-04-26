def solve():
    max_house = 0
    house_set = set()
    for r in range(n):
        for c in range(n):
           if maps[r][c]: house_set.add((r, c))

    for i in range(2 * (n - 1) + 1):
        cost = (i+1) ** 2 + i ** 2
        for r in range(n):
            for c in range(n): # 기준점이 되는 for문
                count = 0
                for r2, c2 in house_set:
                        if abs(r2 - r) + abs(c2 - c) <= i:
                            count += 1
                if count * m >= cost and max_house < count:
                    max_house = count
    return max_house

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
solve()