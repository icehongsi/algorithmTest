import time
import sys
import heapq
def solution(board):
    global answer
    visited = [[False] * len(board)] * len(board)
    answer = 500 * (len(board) ** 2)
    def backtracking(row, col, money, visited):
        print("func", row, col, money)
        global answer
        if (row, col) == (len(board)- 1, len(board) - 1) or money > answer:
            if answer > money:
                answer = money
            return

        if (row, col) != (0, 0):
            money += 500

        temp = money
        print(temp)
        for i in visited:
            print(i)

        if row + 1 < len(board) and not board[row + 1][col] and not visited[row+1][col]: #동쪽
            print("동")
            while row + 1 < len(board) and not board[row + 1][col]:
                visited[row][col] = True
                temp += 100
                row += 1
            backtracking(row, col, temp, visited)
            temp = money

        if col + 1 < len(board) and not board[row][col + 1] and not visited[row][col + 1]: #남쪽
            print("남")
            while col + 1 < len(board) and board[row][col + 1] == 0:
                visited[row][col] = True
                temp  += 100
                col += 1
            backtracking(row, col, temp, visited)
            temp = money



        if row - 1 >= 0 and not board[row - 1][col] and not visited[row - 1][col]: #서쪽
            print("서")
            while row - 1 >= 0 and board[row - 1][col] == 0:
                visited[row][col] = True
                temp  += 100
                row -= 1
            backtracking(row, col, temp, visited)
            temp = money

        if col - 1 >= 0 and not board[row][col - 1] and not visited[row][col - 1]: #북쪽
            print("북")
            while col - 1 >= 0 and board[row][col - 1] == 0:
                visited[row][col] = True
                temp += 100
                col -= 1
            backtracking(row, col, temp, visited)
            temp = money


    backtracking(0, 0, 0, visited)

    return answer

def solution(board):
    visited = [[False] * len(board)] * len(board) #방문 여부를 나타냄
    cost = [[sys.maxsize] * len(board)] * len(board) # 각 노드가 도달하는 데 필요한 값을 나타냄
    cost[0][0] = 0
    costEstimate = lambda x, direction: 500 if x not in (0, direction) else 100

    def dijkstra(row, col, direction = 0):
        if board[row][col+1] == 0 and not visited[row][col+1]: # 남쪽
            money = cost[row][col] + costEstimate(1, direction)
            if cost[row][col+1] > money:
                cost[row][col+1] = money

        if board[row][col-1] == 0 and not visited[row][col-1]: # 북쪽
            money = 
        if board[row+1][col] == 0 and not visited[row+1][col]: # 동쪽
        if board[row-1][col] == 0 and not visited[row-1][col]: # 서쪽


print(solution([[0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,0,0],
                [0,0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0,1],
                [0,0,1,0,0,0,1,0],
                [0,1,0,0,0,1,0,0],
                [1,0,0,0,0,0,0,0]]))