def solution(N, number):
    if N == number:
        return 1
    # 이어붙이기, 더하기, 빼기, 곱하기, 나누기
    dp = [set() for _ in range(8)]
    for i, x in enumerate(dp, start=1):
        x.add(int(str(N) * i))

    for i in range(1, 8):
        dp[i] = {int(str(N) * (i + 1))}
        for j in range(i):
            for x1 in dp[j]:
                for x2 in dp[i-j-1]:
                    dp[i].add(x1 + x2)
                    dp[i].add(x1 - x2)
                    dp[i].add(x1 * x2)
                    if x2 != 0: dp[i].add(x1 // x2)
            if number in dp[i]:
                return i+1


    return -1


print(solution(5, 5))