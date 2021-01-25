def sol(n, m):
    elements = []
    def dfs(remained):
        if len(elements) == m:
            print(" ".join(elements))
            return
        for i in remained:
            next_remained = remained[:]
            next_remained.remove(i)
            elements.append(str(i))
            dfs(next_remained)
            elements.pop()

    dfs(list(range(1, n+1)))

n, m = map(int, input().split())
sol(n, m)