import time
def desert_rotation(): #spread를 반시계방향으로 90도 회전하는 함수
    desert_temp = [[0] * n for i in range(n)]
    for r in range(n):
        for c in range(n):
            desert_temp[c][n - r - 1] = desert[r][c]

    desert[:] = desert_temp


def blow(row, col):
    global answer
    remnant =
    for r in range(row-2, row+3):
        for c in range(col-2, col+3):
            remnant += int(spread[r - row + 2][c - col + 2] * desert[row][col])
            if 0 <= r < n and 0 <= c < n: #범위를 벗어나지 않았을 경우
                desert[r][c] += int(spread[r - row + 2][c - col + 2] * desert[row][col])
            else: #범위를 벗어났을 경우
                answer += int(spread[r - row + 2][c - col + 2] * desert[row][col])

    if 0 <= col - 1 < n and 0 <= row < n: #알파가 범위 내에 있는 경우
        desert[row][col-1] += (desert[row][col] - remnant)
    else: #범위 내에 없는 경우
        answer += (desert[row][col] - remnant)
    desert[row][col] = 0

def solve():
    r = c = n // 2
    move = 1 #이동 축: 서 / 남 / 동 / 북
    #1. 바람이 부는 것을 적용한다

    while True:
        for i in range(1, move + 1): #한 쪽 방향에 대한 바람의 움직임을 적용
            blow(r, c - i)
        # rotation
        desert_rotation()
        temp = r
        r = c - i
        c = n - temp - 1

        for i in range(1, move + 1):
            blow(r, c - i)
        desert_rotation()
        temp = r
        r = c - i
        c = n - temp - 1


        if r == 0 and move == n-1:
            for i in range(1, move + 1):
                blow(r, c - i)
            return desert[r][c]

        move += 1



n = int(input())
desert = [list(map(int, input().split())) for _ in range(n)]
spread = [[0, 0, 0.02, 0, 0,],
          [0, 0.1, 0.07, 0.01, 0],
          [0.05, 0, 0, 0, 0],
          [0, 0.1, 0.07, 0.01, 0],
          [0, 0, 0.02, 0, 0]]
answer = 0


solve()

print(answer)

print("*" * 100)

import sys
n = int(input())
board = [[int(x) for x in input().split()] for _ in range(n)]

ans = 0 # 격자 바깥으로 나간 모래의 양

# 바람의 방향에 따른 모래 비율
rate_left = [[0,0,2,0,0],[0,10,7,1,0],[5,'a',0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
rate_down = [[0,0,0,0,0],[0,1,0,1,0],[2,7,0,7,2],[0,10,'a',10,0],[0,0,5,0,0]]
rate_right = [[0,0,2,0,0],[0,1,7,10,0],[0,0,0,'a',5],[0,1,7,10,0],[0,0,2,0,0]]
rate_up = [[0,0,5,0,0],[0,10,'a',10,0],[2,7,0,7,2],[0,1,0,1,0],[0,0,0,0,0]]

# 모래 이동
def spread(ans,board,rate,nx,ny):
    # Y의 좌표를 rate 배열의 좌표와 함께 대응할 수 있도록 좌표이동? 해준다.
    a,b = nx-2, ny-2

    temp = 0 # Y에서 빠져 나간 모래의 총 양
    for i in range(5):
        for j in range(5):
            #
            if rate[i][j] != 'a' and rate[i][j] != 0:
                if -1 < i+a < n and -1 < j+b < n:
                    board[i+a][j+b] += board[nx][ny]*rate[i][j]//100
                else:
                    # 범위 안에 들어오지 않을 경우
                    ans += board[nx][ny]*rate[i][j]//100
                # a 자리에 모래를 채우기 위해서 빠져나가는 모래의 양을 temp 에 계속 더해준다.
                temp += board[nx][ny]*rate[i][j]//100
            # a 자리의 좌표를 기억
            elif rate[i][j] == 'a':
                remain = (i,j)
    # 나머지 a 부분 처리
    if -1 < remain[0]+a < n and -1 < remain[1]+b < n:
        board[remain[0]+a][remain[1]+b] += board[nx][ny] - temp
    else: # a 자리도 격자 바깥일 경우 격자 바깥으로 나가는 ans에 더해준다.
        ans += board[nx][ny] - temp
    # y 자리 0으로 초기화
    board[nx][ny] = 0
    return board, ans

# 처음 시작 좌표
x,y = n//2,n//2

# 왼쪽 아래 오른쪽 위
dir = [(0,-1),(1,0),(0,1),(-1,0)]
# 왼 아래 - 오른 오른 위 위 / 왼 왼 왼 아래 아래 아래 - 오른 오른 오른 오른 위 위 위 위
# dir[1]일때랑 dir[3]일때 한 time 씩 늘어난다.
time = 1
flag = 0
while flag != 1:
    for i in range(4):
        dx, dy = dir[i]
        for j in range(time):
            x, y = x+dx, y+dy
            if i == 0: # 왼쪽
                board, ans = spread(ans,board,rate_left,x,y)
            elif i == 1: # 아래
                board, ans = spread(ans,board,rate_down,x,y)
            elif i == 2: # 오른쪽
                board, ans = spread(ans,board,rate_right,x,y)
            elif i == 3: # 위에
                board, ans = spread(ans,board,rate_up,x,y)


            for p in board:
                print(p)
            print(ans)
            print("-" * 50)


            if (x, y) == (0,0): # 0,0 으로 왔을때 종료
                flag = 1
                break
        if i == 1 or i == 3: # 1,3 일때 time 늘려주기
            time += 1
        if flag == 1:
            print(ans)
            break

