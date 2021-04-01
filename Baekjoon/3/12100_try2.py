# 바둑판을 움직이는 함수

def move(x, y, dx, dy):
    global board
    if x + dx < 0 or x + dx >= len(board) or y + dy < 0 or y + dy >= len(board):
        return [x, y]

    if board[x + dx][y + dy] == 0: #비어있을 경우
        board[x + dx][y + dy] = board[x][y]
        board[x][y] = 0
        move(x + dx, y + dy, dx, dy)

    elif board[x + dx][y + dy] == board[x][y]: #같을 경우 >> multiply
        board[x + dx][y + dy] = 2 * board[x][y]
        board[x][y] = 0
        temp = {(0, -1): move(x, len(board) - 1, dx, dy),
         (0, 1): move(x, 0, dx, dy),
         (1, 0): move(0, y, dx, dy),
         (-1, 0): move(len(board) - 1, y, dx, dy)}
        temp[(dx, dy)]

    return [x, y]
    #다를 경우 그대로 놔두기


def solution(board):





board = [list(map(int, input().split())) for _ in range(int(input()))]
print(board)