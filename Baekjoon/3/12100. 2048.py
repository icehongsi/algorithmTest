import copy

def solution(board, count = 0):
    global maximum
    mark = False
    if count == 5:
        for i in board:
            if max(i) > maximum:
                maximum = max(i)
        return

    board_to_move = copy.deepcopy(board)

    # 왼쪽으로 이동
    for i in range(len(board)):
        for j in range(len(board)-1, 0, -1):
            if board_to_move[i][j] == board_to_move[i][j-1] or board_to_move[i][j-1] == 0:
                board_to_move[i][j-1] += board_to_move[i][j]
                board_to_move[i][j] = 0

    if board != board_to_move:
        solution(board_to_move, count + 1)
        mark = True
        board_to_move = copy.deepcopy(board)

    # 오른쪽으로 이동
    for i in range(len(board)):
        for j in range(len(board) - 1):
            if board_to_move[i][j] == board_to_move[i][j+1] or board_to_move[i][j+1] == 0:
                board_to_move[i][j+1] += board_to_move[i][j]
                board_to_move[i][j] = 0


    if board != board_to_move:
        solution(board_to_move, count + 1)
        mark = True
        board_to_move = copy.deepcopy(board)

    # 위쪽으로 이동

    for i in range(len(board)-1, 0, -1):
        for j in range(len(board)):
            if board_to_move[i][j] == board_to_move[i-1][j] or board_to_move[i-1][j] == 0:
                board_to_move[i-1][j] += board_to_move[i][j]
                board_to_move[i][j] = 0


    if board != board_to_move:
        solution(board_to_move, count + 1)
        mark = True
        board_to_move = copy.deepcopy(board)



    # 아래쪽으로 이동

    for i in range(len(board) - 1):
        for j in range(len(board)):
            if board_to_move[i][j] == board_to_move[i+1][j] or board_to_move[i+1][j] == 0:
                board_to_move[i+1][j] += board_to_move[i][j]
                board_to_move[i][j] = 0
                i = 0

    if board != board_to_move:
        solution(board_to_move, count + 1)
        mark = True
        board_to_move = copy.deepcopy(board)

    if not mark:
        for i in board:
            if max(i) > maximum:
                maximum = max(i)
        return

board = []
for i in range(int(input())):
    board.append(list(map(int, input().split())))




maximum = 0
solution(board)
print(maximum)


