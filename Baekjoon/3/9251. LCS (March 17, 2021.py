def solution():
    lcs1, lcs2 = " " + input(), " " + input()
    dp = [[0] * len(lcs1) for _ in range(len(lcs2))]


    for r in range(1, len(lcs2)):
        for c in range(1, len(lcs1)):
            if lcs1[c] == lcs2[r]:
                dp[r][c] = dp[r-1][c-1] + 1
            else:
                dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])


    return dp[-1][-1]

print(solution())
