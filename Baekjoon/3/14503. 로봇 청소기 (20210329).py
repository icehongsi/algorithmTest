import sys

def isAccessible(r, c):
    return 1 if 0 <= r < n and 0 <= c < m and not visited[r][c] and room[r][c] != 1 else 0

def solve(r, c, d):
    global count
    mark = True
    # 0: 북 - 서, 1: 동 - 북, 2: 남 - 동, 3: 서 - 남
    rotation = {0: 3, 1: 0, 2: 1, 3: 2} #방향을 시계 반대방향으로 90도 돌리는 함수
    back = {0: 2, 1: 3, 2: 0, 3: 1} #
    direction  = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    if not visited[r][c]:
        count += 1
        visited[r][c] = True

    for _ in range(4):
        d = rotation[d] #시계 반대방향으로 90도만큼 시야를 돌리기
        dr, dc = direction[d]
        if isAccessible(r+dr, c+dc): #시야를 돌려서 해당 부분이 방문하지 않은 경우:
            mark = False
            d = solve(r+dr, c+dc, d)

    if mark: #4군데를 돌아보았으나 모두 방문한 노드인 경우
        dr, dc = direction[back[d]] # 반대 방향으로 방향 전환
        if room[r + dr][c + dc] == 1: # 뒤에 벽이 있을 경우
            print(count) # 지금까지 청소한 타일의 수를 출력
            sys.exit() #강제 종료
        else:
            solve(r + dr, c + dc, d)


n, m = map(int, input().split()) # n: 세로 (행의 길이), m: 가로 (열의 길이)
r, c, d = map(int,input().split())
room = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
count = 0
solve(r, c, d)