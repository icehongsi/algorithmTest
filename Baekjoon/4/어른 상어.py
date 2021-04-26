
def solve():
    n, m, k = map(int, input().split())  # 격자의 크기, 상어의 숫자, 냄새 지속 시간
    maps = [list(map(int, input().split())) for _ in range(n)]
    shark = [[[] for _ in range(n)] for _ in range(n)]
    smell = [[[] for _ in range(n)] for _ in range(n)]  # 지속 시간, 냄새
    start = list(map(int, input().split()))
    for r in range(n):
        for c in range(n):
            if maps[r][c] > 0:
                shark[r][c].append([maps[r][c], start[maps[r][c] - 1]]) #number, 방향

    priority = {}
    for i in range(1, m + 1):
        priority[i] = dict()
        for j in range(1, 5):
            priority[i][j] = list(map(int, input().split()))

    shark_number = m
    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]
    for idx in range(1001):
        for r in range(n):
            for c in range(n):
                if smell[r][c] and smell[r][c][0] == idx:
                    smell[r][c] = []
        temp = [[[] for _ in range(n)] for _ in range(n)]
        '''

        for i in shark:
            print(i)
        print("-" * 50)
        for i in smell:
            print(i)
        print("-" * 50)
        '''

        for r in range(n):
            for c in range(n):
                if shark[r][c]: #상어가 있을 경우:
                    '''
                    if idx == 23:
                        for i in temp:
                            print(i)
                        print("-" * 50)
                        for i in shark:
                            print(i)
                        print("-" * 50)
                        for i in smell:
                            print(i)
                        print("-" * 50)
                    '''

                    number, move = shark[r][c][0]
                    smell[r][c] = [idx + k, number] # 냄새 남기기
                    mr, mc = None, None
                    for i in priority[number][move]: # i번째에 대응되는 d 추출 후
                        if 0 <= r + dr[i] < n and 0 <= c + dc[i] < n and not smell[r + dr[i]][c + dc[i]]: # 아무 냄새가 없을 경우
                            mr, mc = r + dr[i], c + dc[i]
                            break
                    if mr == mc == None: # 자기 냄새 찾기
                        for i in priority[number][move]:
                            if 0 <= r + dr[i] < n and 0 <= c + dc[i] < n and smell[r + dr[i]][c + dc[i]][1] == number:
                                mr, mc = r + dr[i], c + dc[i]
                                break
                    # mr, mc로 상어가 이동하게 됨
                    shark[r][c][-1][-1] = i


                    temp[mr][mc].append(shark[r][c].pop())
                    if len(temp[mr][mc]) > 1:
                        if temp[mr][mc][0][0] < temp[mr][mc][1][0]:
                            temp[mr][mc].pop()
                        else:
                            temp[mr][mc].pop(0)
                        shark_number -= 1
                        if shark_number == 1:
                            print(idx + 1)
                            return
                    elif shark[mr][mc]:
                        if temp[mr][mc][0][0] < shark[mr][mc][1][0]:
                            shark[mr][mc].pop()
                        else:
                            temp[mr][mc].pop()
                        shark_number -= 1
                        if shark_number == 1:
                            print(idx + 1)
                            return



        shark = temp
    print(-1)
    return

solve()
