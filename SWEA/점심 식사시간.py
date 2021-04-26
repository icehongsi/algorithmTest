from itertools import product
from collections import deque

def solve():
    ans = float('inf') # 0. 시간은 초기에 무한으로 설정
    people, stair = [], []
    for r in range(N): # 1. 사람과 계단 찾기
        for c in range(N):
            if info[r][c] > 1:
                stair.append((r, c, info[r][c]))
            elif info[r][c] == 1:
                people.append((r, c))

    distance = [] # distance의 i번째 원소는 i번쨰 사람의 계단 1, 계단 2와의 맨하탄 거리를 포함하고 있음
    for r, c in people:
        dist1 = abs(stair[0][0] - r) + abs(stair[0][1] - c) + 1
        dist2 = abs(stair[1][0] - r) + abs(stair[1][1] - c) + 1
        distance.append((dist1, dist2))

    for order in tuple(product([0, 1], repeat= len(people))): #1. 모든 경우의 수에 대한 반복
        sub_ans = 0
        stair_use_queue = [deque([]), deque([])]
        stair_waiting_queue = [[], []]
        for k, v in enumerate(order): # k번쨰 사람은 v번쨰 계단을 이용하게 되므로,
            stair_waiting_queue[v].append(distance[k][v]) #V번째 계단을 기다리는 큐에 k번쨰 사람의 맨하탄 거리를 넣음
        for i in range(2):
            stair_waiting_queue[i].sort()
            stair_waiting_queue[i] = deque(stair_waiting_queue[i])
            time = 0
            while time < ans and stair_waiting_queue[i]: # 기존의 최솟값을 초과하거나, waiting queue에 사람이 있을 떄까지 반복
                # 1) 제거
                while stair_use_queue[i] and stair_use_queue[i][0] == time: # 계단을 이용하는 사람이 있으면서 다 내려올 시간이 되었을 경우
                    stair_use_queue[i].popleft() # 조건에 해당하는 사람이 없어질 때까지 제거
                # 2) 삽입
                while len(stair_use_queue[i]) < 3 and stair_waiting_queue[i] and stair_waiting_queue[i][0] <= time: #큐가 비었을 경우 채워주기
                    stair_waiting_queue[i].popleft()
                    stair_use_queue[i].append(time + stair[i][2]) #큐에 입장 시간 + 계단의 길이만큼 더해주기

                # 3) 시간의 흐름 반영
                time += 1

            # Sub Answer: 두 번의 loop 중 최댓값
            if stair_use_queue[i]:
                time = max(stair_use_queue[i])
            sub_ans = max(sub_ans, time)
        # Main Answer: loop를 통해 나온 sub_ans와 ans 중 최솟값
        ans = min(ans, sub_ans)

    return ans

for x in range(int(input())):
    N = int(input())
    info = [list(map(int, input().split())) for i in range(N)]
    solve()
