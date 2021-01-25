
def check_diag(r, c):
    print(r, c)
    if r < 0 or c < 0 or r == n or c == n:
        return False
    #print((check_diag(r - 1, c - 1) and check_diag(r - 1, c + 1)))
    return False if board[r][c] else not(check_diag(r - 1, c - 1) and check_diag(r - 1, c + 1))

board = [[False, True, False, False],
[True, False, False, True],
[True, False, False, False],
[False, False, False, False]]

n = 4
print(check_diag(3, 2))