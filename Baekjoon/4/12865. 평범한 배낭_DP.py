n, k = map(int, input().split())
values = []
for _ in range(n):
    w, v = map(int, input().split())
    value_per_unit = v/w
    values.append([w, v, value_per_unit])

values = sorted(values, key = lambda x: x[0]) #무게 역순으로

dp = [[0] * (n+1) for _ in range(k+1)]


for idx in range(1, n+1):
    for weight in range(1, k+1):
        if values[idx-1] <= weight:
            dp[idx][weight] = max()



