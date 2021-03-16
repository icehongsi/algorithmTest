'''
def solution():
    n, max_weight = map(int, input().split())
    things = []
    for i in range(n): # [0]: 무게, [1]: 가치, [2]: 가성비
        things.append(list(map(int, input().split())))
        things[-1].append(things[-1][1] / things[-1][0])
    things.sort(key = lambda x: x[2], reverse = True) # 가성비가 높은 순으로 정렬
    print(things)

    # 1. 가성비가 높은 순서대로 (무게가 허용되었을 떄) 집어넣을 경우 / 집어넣지 않을 경우를 고려함
    def knapsack(weight, value, idx): #잔여 무게, 현재 가치, 인덱스
        global max_value
        if weight == 0 or idx == len(things): # 바닥 조건
            max_value = max(max_value, value)

        else:
            if weight >= things[idx][0]: # 잔여 무게가 더 많을 경우, 해당 물건을 넣는 것을 고려
                knapsack(weight - things[idx][0], value + things[idx][1], idx + 1)

            knapsack(weight, value, idx + 1) # 넣지 않는 것을 고려

    knapsack(max_weight, 0, 0)
    print(max_value)




max_value = 0
solution()

'''


def solution():
    n, max_weight = map(int, input().split())
    things = [[0,0,0]]
    for i in range(n): # [0]: 무게, [1]: 가치, [2]: 가성비
        things.append(list(map(int, input().split())))
        things[-1].append(things[-1][1] / things[-1][0])
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, max_weight + 1):
            if j >= things[i][0]: # things의 특정 element를 담을 수 있는 용적이 있을 경우
                dp[i][j] = max(dp[i-1][j - things[i][0]] + things[i][1],
                               dp[i-1][j])
                # element를 담지 않을 경우의 이전 최대의 가치, element를 담을 수 있는 용적을 가진 이전 phase일 때의 가치 + 새로 담을 물건의 가치 중 큰 것
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[n][max_weight])

solution()


    # 1. 가성비가 높은 순서대로 (무게가 허용되었을 떄) 집어넣을 경우 / 집어넣지 않을 경우를 고려함




max_value = 0
solution()