def solve(k, idx, value):
    global max_value
    if idx == len(values) or k < values[idx][0]:
        max_value = max(max_value, value)
        return
    # 현재 item을 배낭에 넣는 경우
    solve(k - values[idx][0], idx + 1, value + values[idx][1])
    solve(k, idx + 1 , value)


n, k = map(int, input().split())
values = []
for _ in range(n):
    w, v = map(int, input().split())
    value_per_unit = v/w
    values.append([w, v, value_per_unit])
values = sorted(values, key = lambda x: x[0], reverse = True) #무게 역순으로
max_value = 0
solve(k, 0, 0)
print(max_value)