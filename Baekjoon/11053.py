def solution():
    n = int(input())
    numbers = list(map(int, input().split()))
    dp = [0] * n
    for i in range(1, n):
        dp[i] = 1
        for j in range(i-1, -1, -1):
            if numbers[j] < numbers[j+1]:
                dp[i] = max(dp[i], dp[j+1] + 1)

    print(max(dp))

solution()