from collections import defaultdict
def solve():
    n, lower, upper = map(int, input().split())
    kingdom = [list(map(int, input().split())) for _ in range(n)]
    flag, count = True, 0
    def dfs(r, c, prev = float('inf')):
        if 0 <= r < n and 0 <= c < n and visited[r][c] == 0 and (prev == float('inf') or lower <= abs(kingdom[r][c] - prev) <= upper):
            visited[r][c] = case
            country_list.append((r, c)) #country list에 추가
            dfs(r+1, c, kingdom[r][c])
            dfs(r-1, c, kingdom[r][c])
            dfs(r, c+1, kingdom[r][c])
            dfs(r, c-1, kingdom[r][c])


    while flag:
        flag = False
        visited = [[0] * n for _ in range(n)]
        for i in kingdom:
            print(i)
        print("-" * 50)
        case = 1
        for r in range(n):
            for c in range(n):
                if visited[r][c] == 0:
                    country_list = []
                    dfs(r, c)
                    if len(country_list) > 1:
                        flag = True
                        case += 1
                    else:
                        visited[r][c] = 0
        cases = defaultdict(int)
        for r in range(n):
            for c in range(n):
                if visited[r][c] > 0:
                    cases[visited[r][c]] += kingdom[r][c]
        for i in visited:
            print(i)
        print(cases)
        return
        if flag:
            count += 1
    print(count)


solve()
