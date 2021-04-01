import copy


def solution():
    n = int(input())
    board = [[0] * n for _ in range(n)]


    def backtracking(r = 0):
        global count
        max_num = n
        if r == len(board):

            #for i in board:
            #    print(i)
            #print("-"*50)

            count += 2
            return

        for c in range(max_num): #차례대로 순회
            flag = True

            # 위쪽 (같은열 다른 행) 체크
            for i in range(r-1, -1, -1):
                if board[i][c] == 1:
                    flag = False
                    break
            # 왼쪽 대각선 체크

            r1, c1 = r, c

            while r1 > 0 and c1 > 0:
                r1 -= 1
                c1 -= 1
                if board[r1][c1] == 1:
                    flag = False
                    break

            r1, c1 = r, c
            while r1 > 0 and c1 < len(board) - 1:
                r1 -= 1
                c1 += 1
                if board[r1][c1] == 1:
                    flag = False
                    break

            if flag:
                board[r][c] = 1
                backtracking(r + 1)
                board[r][c] = 0

    backtracking()



count = 0
solution()
print(count)
