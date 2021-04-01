def solve(money, idx = 0): # 현재까지의 돈, 현재 방문하는 인덱스
    global result
    if idx >= len(schedule):
        result = max(money, result)
        return
    # schedule의 k번째 원소: [0]: 일자, [1]: 금액
    # 넣을 경우, 넣지 않을 경우에 대해 모두 따져보기
    if idx + schedule[idx][0] <= n: # 스케줄이 넣어볼 수 있으므로 넣어보기
        solve(money + schedule[idx][1], idx + schedule[idx][0])
    # 넣어보지 않을 경우의 수는 항상 고려할 수 있음
    solve(money, idx + 1)



n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
result = 0
solve(0, 0)
print(result)