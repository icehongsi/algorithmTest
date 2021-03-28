from collections import deque
#로직은 맞았으나, Python 한계로 인하여 오답
def solution():
    n = int(input())
    house = [list(map(int, input().split())) for _ in range(n)]
    prev, curr = [0, 0], [0, 1]  # 초기의 파이프 위치
    q, count = deque([[prev, curr]]), 0

    def checkInvalidity(r, c):
        if r >= n or r < 0 or c >= n or c < 0 or house[r][c] == 1:
            return True
        return False

    while q:
        prev, curr = q.popleft()
        moved = [curr[0] - prev[0], curr[1] - prev[1]]
        if moved == [0, 1]:  # 가로로 배열되어 있을 경우
            row, col = [0, 1], [1, 1]
        elif moved == [1, 1]:  # 대각선으로 배열되어 있을 경우
            row, col = [0, 1, 1], [1, 1, 0]
        else:  # 세로로 배열되어 있을 경우
            row, col = [1, 1], [1, 0]

        for i in range(len(row)):
            r, c = curr[0] + row[i], curr[1] + col[i]

            if checkInvalidity(r, c):  # 조건에 어긋날 경우
                continue

            if [row[i], col[i]] == [1, 1] and (checkInvalidity(r, c-1) or checkInvalidity(r-1, c)):
                continue

            if [r, c] == [n - 1, n - 1]:
                count += 1
                continue

            q.append([curr, [r, c]])

    print(count)


solution()
