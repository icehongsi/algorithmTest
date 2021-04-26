from itertools import combinations
from collections import deque

def solve():
    getDistance = lambda c, er, ec: abs(n - er) + abs(c - ec)
    enemies, ans = [], 0 # 적 리스트 만들기
    for r in range(n):
        for c in range(m):
            if enemy[r][c]:
                enemies.append((r, c))

    for archer in combinations(range(m), 3): # 모든 조합에 대해 고려
        kill = [[], [], []]
        visited = [[0] * m for _ in range(n)]
        count = 0
        for r, c in enemies:
            for i in range(3):
                kill[i].append((getDistance(archer[i], r, c), r, c)) # 각각의 column의 조합에 대해 (거리, 적이 위치한 행과 열)을 삽입한다.
        for i in range(3):
            kill[i].sort(key = lambda x: (x[0], x[2])) #1순위: 거리, 2순위: 열 순으로 정렬한다. 이 경우 같은 거리를 가졌을 때 왼쪽부터 공격하게 된다.
            kill[i] = deque(kill[i])

        for i in range(n): #행이 1 turn당 하나씩 밀린다.
            for k in range(3): # 3명의 궁수에 대해 죽일 적이 있으면 죽이고, 그렇지 않으면 죽이지 않는 것으로 한다.
                while kill[k] and kill[k][0][1] > (n - 1 - i): # 죽일 적 중 이미 행을 넘어서버려 없어진 적 삭제
                    kill[k].popleft()
                while kill[k] and kill[k][0][0] <= d + i: # 사정거리 안에 있는 경우 겨냥
                    x, r, c = kill[k].popleft() #추출
                    if r > (n - 1 - i) or 0 < visited[r][c] < i+1: #이 경우 이미 행을 넘어가 버렸거나, 다른 궁수가 이전에 죽인 케이스이다.
                        continue # 다시 겨냥하도록 한다.
                    if visited[r][c] == 0: # 이 경우는 처음 죽이는 것이다.
                        visited[r][c] = i+1 # i+1번째에 죽였음을 체크한다.
                        count += 1
                    break
        ans = max(count, ans)
    return ans

n, m, d = map(int, input().split())
enemy = [list(map(int, input().split())) for _ in range(n)]
print(solve())