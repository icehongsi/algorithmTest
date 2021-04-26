from collections import deque


def solution(board):
    answer = 0
    def isValid(r, c):
        d = [(-1, -1), (0, -1), (-1, 0)]
        min_value = float('inf')
        for x, y in d:
            if 0 <= r + x < len(board) and 0 <= c + y < len(board[0]) and board[r+x][c+y]:
                min_value = min(min_value, board[r+x][c+y])
            else:
                min_value = 0
        return min_value + 1
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c]:
                board[r][c] = isValid(r, c)
                answer = max(board[r][c], answer)

    return answer

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))