from collections import deque
'''
1. r, c에 대해, 연결 가능한 모든 지형에 대해 하나라도 연결되어있는지 확인한다.
1 - 2. 연결되어있지 않을 경우 건너뛰기
2. 방문한 부분을 제외한 모든 연결 가능한 부분을 queue에 넣는다.
'''

def bfs():
    ans = 0
    q = deque([[mr, mc, maps[mr][mc]]])
    for i in range(1, l + 1):
        qlen = len(q)
        while q and qlen:
            r, c, pipe = q.popleft()

            if not visited[r][c]:

                visited[r][c] = 1
                for j in check[pipe]:
                    tr, tc = r + d[j][0], c + d[j][1]
                    if 0 <= tr < row and 0 <= tc < col and not visited[tr][tc] and maps[tr][tc] > 0:# and reverse[j] in check[maps[tr][tc]]:
                        if reverse[j] in check[maps[tr][tc]]:
                            print(r, c, tr, tc)
                        # 해당 지역에 있는 파이프가 연결될 경우
                            q.append([tr, tc, maps[tr][tc]])
            qlen -= 1
    for i in visited:
        ans += sum(i)
    return ans




check = {0: [],
        1: [0,1,2,3],
         2: [0, 2],
         3: [1, 3],
         4: [1,2],
         5: [0,1],
         6: [0,3],
         7: [2,3]}
d = [(1,0), (0, 1), (-1,0), (0, -1)]
reverse = [2, 3, 0, 1]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    row, col, mr, mc, l = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(row)]
    visited = [[0] * col for _ in range(row)]
    print(f"#{test_case} {bfs()}")