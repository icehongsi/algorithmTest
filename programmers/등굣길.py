def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    for col, row in puddles:
        dp[row][col] = -1
    for i in range(1, n+1):
        for j in range(1, m+1):
            print(i, j)
            print(dp)
            if dp[i][j] == -1:
                dp[i][j] = 0
            elif i == 1 and j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][m] % 1000000007

print(solution(4,3,[[2,2]]))