def solution(n, costs):
    connected = {}
    result, head = 0, 0

    def find(key): # union-find와 같은 연산 실행
        if key not in connected:
            return
        while key != connected[key]:
            key = connected[key]
        return key

    for cost in sorted(costs, key = lambda x: x[2]):
         #0: 시작, 1: 종료, 2:건설비용
        node_1, node_2 = find(cost[0]), find(cost[1])
        if node_1 == node_2 == None: #전혀 새로운 것
            connected[cost[1]] = cost[0]
            connected[cost[0]] = cost[0]
            head += 1
        elif node_1 == None:
            connected[cost[0]] = cost[1]
        elif node_2 == None:
            connected[cost[1]] = cost[0]
        elif node_1 != node_2:
            connected[node_1] = node_2
            head -= 1
        else:
            continue

        result += cost[2]

        if len(connected.keys()) == n and head == 1: #top node가 하나이면서 keys의 개수가 n과 일치할 때에는 종료
            return result




solution(4, [[0,1,1],[0,2,2],[2,3,1]])
print("-"*50)
solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])