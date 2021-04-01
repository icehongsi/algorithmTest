def isValidCoordinate(r, c):
    return 1 if 0 <= r < n and 0 <= c < m and not (r,c) in visited else 0

def getMiddleFingerShapeTetromino(r, c):
    global maximum
    answer = []
    for dr, dc in d:
        if isValidCoordinate(r + dr, c + dc):
            answer.append(array[r+dr][c+dc])
    if len(answer) == 3:
        maximum = max(maximum, sum(answer) + array[r][c])
    elif len(answer) == 4:
        maximum = max(maximum, array[r][c] + sum(answer) - min(answer))

def dfs(r, c, depth = 0, score = 0):
    global maximum
    if depth == 4: #base case: 더이상 순회할 필요 없으므로 backtrack
        maximum = max(maximum, score)
        return
    visited.add((r, c)) # 중복하여 방문하지 않도록 방문 리스트에 추가한다.
    score += array[r][c]
    for dr, dc in d:
        if isValidCoordinate(r + dr, c + dc):
            dfs(r + dr, c + dc, depth + 1, score) # 유효한 타일일 경우 방문
    visited.remove((r, c)) # 모든 과정이 끝났으면 방문했다는 사실을 지운다.

def solve():
    for r in range(n):
        for c in range(m):
            dfs(r, c)
            getMiddleFingerShapeTetromino(r, c)
    print(maximum)

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
visited = set()
answer = []
maximum = 0
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
solve()