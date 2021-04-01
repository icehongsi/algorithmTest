'''
from collections import deque
def solution():
    scores = [int(input()) for i in range(int(input()))] # 점수 모음

    if len(scores) <= 2:
        print(sum(scores))
        return

    dp1 = deque([scores[0], scores[0]+scores[1]])  #  직전에 한 칸 올랐을 경우의 수
    dp2 = deque([0, scores[1]])  #  직전에 두 칸 올랐을 경우의 수

    for i in range(2, len(scores)):
        dp2.append(max(dp1[-2], dp2[-2]) + scores[i])
        dp1.append(dp2[-2] + scores[i])

        dp1.popleft()
        dp2.popleft()

    print(max(dp1[-1], dp2[-1]))

solution()




#deque 미적용

def solution():
    scores = [int(input()) for i in range(int(input()))] # 점수 모음

    if len(scores) <= 2:
        print(sum(scores))
        return

    dp1 = [scores[0], scores[0]+scores[1]]  #  직전에 한 칸 올랐을 경우의 수
    dp2 = [0, scores[1]]  #  직전에 두 칸 올랐을 경우의 수

    for i in range(2, len(scores)):
        dp2.append(max(dp1[-2], dp2[-2]) + scores[i])
        dp1.append(dp2[-2] + scores[i])

    print(max(dp1[len(scores)-1], dp2[len(scores)-1]))

solution()

'''
# 배열 미사용

def solution():
    n = int(input())
    if n <= 2:
        print(sum([int(input()) for _ in range(n)]))
        return

    prev_1 = int(input()) #  직전에 한 칸 올랐을 경우의 수
    curr_1 = prev_1 + int(input())

    prev_2 = 0 #  직전에 두 칸 올랐을 경우의 수
    curr_2 = curr_1 - prev_1

    for i in range(2, n):
        value = int(input())
        temp = prev_2
        prev_2, curr_2 = curr_2, max(prev_1, prev_2) + value
        prev_1, curr_1 = curr_1, temp + value



    print(max(curr_1, curr_2))

solution()