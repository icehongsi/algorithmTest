
def solution(n):
    dp = [0,1,1,1]

    if n < 4:
        return dp[n]

    for i in range(4, n+1):
        dp.append(dp[1] + dp[2])
        dp.pop(0)
    return dp[-1]




testCase = [int(input()) for _ in range(int(input()))]

for i in testCase:
    print(solution(i))