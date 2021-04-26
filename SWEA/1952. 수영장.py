def solve():
    #1. 변수 선언
    day, month, three, year = map(int, input().split())
    schedule = list(map(int, input().split()))
    cost_list =  []
    def dfs(idx, cost):
        if idx == 12:
            cost_list.append(cost)
            return
        if idx + 3 <= 12:
            dfs(idx + 3, cost + three)
        if idx + 12 <= 12:
            dfs(idx + 12, cost + year)
        dfs(idx + 1, cost + day * schedule[idx])
        dfs(idx + 1, cost + month)

    dfs(0, 0)
    return min(cost_list)


solve()