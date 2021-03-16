#Dynamic Programming

def solution():
    n = int(input())
    dp = [0, 0, 1, 1] # dp[i]: 자연수 i를 만들기까지 필요한 최소연산 수

    for i in range(4, n+1):
        candidate = [dp[-1] + 1]
        if i % 3 == 0:
            candidate.append(dp[int(i/3)] + 1) # 3으로 나누어 떨어질 경우 i / 3에 대하여 고려
        if i % 2 == 0:
            candidate.append(dp[int(i/2)] + 1) # 2으로 나누어 떨어질 경우 i / 2에 대하여 고려

        dp.append(min(candidate))

    return dp[n]

print(solution())