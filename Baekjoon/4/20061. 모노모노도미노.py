def solve():
    n = int(input())
    green = [[0] * 4 for _ in range(6)]
    blue = [[0] * 4 for _ in range(6)]
    score = 0

    for _ in range(n):
        #1. 도미노 삽입
        domino, r, c = map(int, input().split())
        if domino == 1: #type 1
            green[0][c] = 1
            blue[0][3-r] = 1
        elif domino == 2: # type 2: green: 가로로 긴 도미노, blue: 세로로 긴 도미노
            green[0][c], green[0][c+1] = 1, 1
            blue[0][3 - r], blue[1][3 - r] = 1, 1

        elif domino == 3: #type 3: green: 세로로 긴 도미노, blue: 가로로 긴 도미노
            green[0][c], green[1][c] = 1, 1
            blue[0][3 - r], blue[0][2 - r] = 1, 1

        #2. 도미노 배열
        for color in (blue, green):
            if domino == 1:
                row, col = 0, color[0].index(1)
                while row+1 < 6 and color[row+1][col] == 0:
                    color[row + 1][col] = 1
                    color[row][col] = 0
                    row += 1

            elif (color == blue and domino == 3) or (color == green and domino == 2): # 세로로 긴 도미노 상대
                row, col = 0, color[0].index(1)
                while row + 1 < 6 and color[row + 1][col] == color[row + 1][col + 1] == 0:
                    color[row + 1][col], color[row + 1][col + 1] = 1, 1
                    color[row][col], color[row][col + 1] = 0, 0
                    row += 1

            elif (color == blue and domino == 2) or (color == green and domino == 3): #가로로 긴 도미노 상대
                row, col = 1, color[0].index(1)
                while row + 1 < 6 and color[row + 1][col] == 0:
                    color[row + 1][col] = 1
                    color[row - 1][col] = 0
                    row += 1


            #3. 점수 획득
            for i in range(6):
                if sum(color[i]) == 4: #꽉 찼을 경우
                    score += 1
                    color.pop(i)
                    color.insert(0, [0] * 4)

            for i in range(2):
                if sum(color[i]) > 0: #위가 비어있지 않은 경우
                    color.pop()
                    color.insert(0, [0] * 4)

    tiles = 0
    for color in (blue, green):
        for i in color:
            tiles += sum(i)

    print(score, tiles, sep = "\n")






solve()
