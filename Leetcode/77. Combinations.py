def solve(n, k):
    ans = []
    def dfs(numbers = [], idx = 1):
        if len(numbers) == k:
            print(numbers)
            ans.append(numbers[:])
            return
        for i in range(idx, n+1):
            dfs(numbers + [i], i + 1)
    dfs()
    print(ans)

solve(4, 2)