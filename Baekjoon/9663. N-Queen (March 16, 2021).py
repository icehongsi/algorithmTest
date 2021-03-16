import copy


def solution(r):
    global board, count
    if r == len(board): #다 도달하였을 때
        count += 1

    for c in range(len(board)):
        print(r, c)
        if sum(board[x][c] for x in range(r))\
            or sum(board[r - x][c + x] for x in range(min(r, len(board) - c - 1), 1))\
                or sum(board[r - x][c - x] for x in range(1, min(r, c) + 1)):
            continue

        board[r][c] = 1
        solution(r + 1)
        board[r][c] = 0





board = [[0] * 5 for _ in range(int(input()))]
count = 0
solution(0)
print(count)




print(board)