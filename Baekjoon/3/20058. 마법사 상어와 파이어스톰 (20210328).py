import sys
sys.setrecursionlimit(10**5)

def rotation(x, y, ex, ey):
    rotated = [[] for _ in range(ex - x + 1)]
    for r in range(ex, x - 1, -1):
        for c in range(y, ey + 1):
            rotated[c % (ex - x + 1)].append(ice[r][c])

    for r in range(x, ex + 1):
        for c in range(y, ey + 1):
            ice[r][c] = rotated[r % (ex - x + 1)][c % (ey - y + 1)]


def isOccupied(r, c):
    if r >= len(ice) or r < 0 or c >= len(ice) or c < 0 or ice[r][c] == 0:
        return 0
    return 1


def dfs(r, c):
    global chunk_size, value
    if 0 <= r < len(ice) and 0 <= c < len(ice) and ice[r][c] > 0 and (not visited[r][c]):
        visited[r][c] = True
        chunk_size += 1;
        value += ice[r][c]
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)


def solution():
    global max_chunk, chunk_size, value

    for x in rotate: # 매 rotate마다 한 번씩 시행
        q = []
        for r in range(0, len(ice), 2 ** x): #1. rotation 실행
            for c in range(0, len(ice), 2 ** x):
                rotation(r, c, r + 2 ** x - 1, c + 2 ** x - 1)
        for r in range(len(ice)): #2. 주변에 얼음이 3개 미만일 경우
            for c in range(len(ice)):
                if sum([isOccupied(r+1, c), isOccupied(r-1, c), isOccupied(r, c+1), isOccupied(r, c-1)]) < 3:
                    q.append([r, c]) # queue에 추가
        for r, c in q: #3. queue를 순회하며 ice를 1씩 감소
            if ice[r][c] != 0:
                ice[r][c] -= 1

    # 4. 가장 큰 얼음덩어리 체크
    for r in range(2 ** n):
        for c in range(2 ** n):
            if (not visited[r][c]) and ice[r][c] > 0:
                chunk_size = 0
                dfs(r, c)
                max_chunk = max(max_chunk, chunk_size)

    print(value, max_chunk, sep = "\n")





n, q = map(int, input().split())
ice = [list(map(int, input().split())) for i in range(2 ** n)]
rotate = list(map(int, input().split()))
max_chunk, value, chunk_size = 0, 0, 0
visited = [[False] * 2 ** n for _ in range(2 ** n)]
solution()