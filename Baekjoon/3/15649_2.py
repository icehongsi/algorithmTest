import time
def check_diag_left(r, c):
    while r >= 0 and c >= 0:
        if board[r][c]:
            return False
        r -= 1
        c -= 1
    return True


def check_diag_right(r, c):
    while c < n and r >= 0:
        if board[r][c]:
            return False
        c += 1
        r -= 1
    return True

def check_hor(r, c):
    return True if not sum([board[i][c] for i in range(r-1, -1, -1)]) else False

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

n = int(input())
board = [[False for _ in range(n)] for _ in range(n)]
result = 0

nqueens(0)
print(result)