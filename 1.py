import sys


def solution():
    global maximum
    n, k = map(int, input().split())  # n: 열 및 행 수, k: 최대로 깎을 수 있는 깊이
    mountain = [list(map(int, input().split())) for _ in range(n)]  # 등산로
    visited = [[False] * n for _ in range(n)]
    maximum_value = max([max(i) for i in mountain])

    # 산을 깎을 경우 지나갈 수 있을 지 물어보는 함수
    def isValidPath(r, c, prev_value, path_length):
        #print("function isvalidpath: ", r, c, prev_value, path_length)
        global maximum, flag
        if r < 0 or c < 0 or r >= n or c >= n or visited[r][c]:
            return  # 여태까지 찾은 경로 중 최댓값일 경우 값 교체

        if mountain[r][c] < prev_value:  # 더 낮은 경우
            visited[r][c] = True
            dfs(r, c, mountain[r][c], path_length + 1)
            visited[r][c] = False
        elif mountain[r][c] >= prev_value and flag and prev_value > mountain[r][c] - k:  # 높이차이는 있으나 진행 가능한경우
            flag, visited[r][c] = False, True
            dfs(r, c, prev_value - 1, path_length + 1)
            flag, visited[r][c] = True, False
        else:
            #print(r, c, path_length)
            if path_length > maximum:
                maximum = max(path_length, maximum)

    def dfs(r, c, value=maximum_value, path_length=1):
        #print("function dfs: ",r, c, value, path_length)
        isValidPath(r - 1, c, value, path_length)
        isValidPath(r + 1, c, value, path_length)
        isValidPath(r, c + 1, value, path_length)
        isValidPath(r, c - 1, value, path_length)

    for r in range(n):
        for c in range(n):
            if mountain[r][c] == maximum_value:
                visited[r][c] = True
                dfs(r, c)
                visited[r][c] = False

    return maximum

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    maximum = 0
    flag = True
    # ///////////////////////////////////////////////////////////////////////////////////
    print("#{0} {1}".format(test_case, solution()))
    # ///////////////////////////////////////////////////////////////////////////////////
