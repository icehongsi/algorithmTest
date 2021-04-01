import time
def check_diag_left(r, c):
    if r < 0 or c < 0:
        return True
    return False if board[r][c] else check_diag_left(r - 1, c - 1)

def check_diag_right(r, c):
    if r < 0 or c < 0 or c == n:
        return True
    return False if board[r][c] else check_diag_right(r - 1, c + 1)

def check_hor(r, c):
    if r < 0:
        return True
    return False if board[r][c] else check_hor(r - 1, c)

def nqueens(r):
    global result
    if r == n:
        return True
    for c in range(n):
            if check_diag_left(r,c) and check_diag_right(r, c) and check_hor(r,c):
                board[r][c] = True
                if nqueens(r+1):
                    result += 1
                board[r][c] = False
    return

#n = int(input())
for i in range(1, 11):
    n = i
    print("n: ", n)
    board = [[False for _ in range(n)] for _ in range(n)]
    result = 0

    nqueens(0)
    print(result)