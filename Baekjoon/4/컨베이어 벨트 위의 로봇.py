from collections import deque

def solve():
    n, k = map(int, input().split())
    belt = deque(map(int, input().split()))
    robot = deque([0] * n)
    zero = 0
    count = 0
    while zero < k:
        count += 1
        robot.rotate(1) # robot 및 belt 회전
        belt.rotate(1)
        robot[n-1] = 0 #내리는 위치의 로봇 내리기

        for i in range(n-2, 0, -1):
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] > 0:
                robot[i], robot[i+1] = robot[i+1], robot[i]
                belt[i+1] -= 1
                if belt[i+1] == 0:
                    zero += 1
        robot[n-1] = 0
        if belt[0] > 0 and robot[0] == 0:
            robot[0] += 1
            belt[0] -= 1
            if belt[0] == 0:
                zero += 1



    print(count)





solve()