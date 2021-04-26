from _collections import defaultdict
def solve():
    n, m, k = map(int, input().split())  # 셀의 개수, 격리 시간, 미생물 군집 개수
    microOrganizm = defaultdict(list)
    for _ in range(k):
        p, q, r, s = map(int, input().split())
        microOrganizm[(p, q)].append([r, s])
    d = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
    dt = {1 : 2, 2: 1, 3: 4, 4: 3}

    for _ in range(m):
        temp = defaultdict(list) # 임시 배열 선언
        for r, c in microOrganizm:
            number, move = microOrganizm[(r,c)][0]
            tr, tc = r + d[move][0], c + d[move][1]
            if tr in (0, n-1) or tc in (0, n-1):
                temp[(tr, tc)].append([number // 2, dt[move]])
            else:
                temp[(tr, tc)].append([number, move])
        for r, c in temp:
            if len(temp[(r, c)]) > 1:
                max_value, total, direction = 0, 0, 0
                while temp[(r, c)]:
                    number, move = temp[(r, c)].pop()
                    total += number
                    if max_value < number:
                        max_value = number
                        direction = move
                temp[(r, c)].append([total, direction])
        microOrganizm = temp

    return sum(microOrganizm[i][0][0] for i in microOrganizm)

for i in range(int(input())):
    print(solve())
    print("-" * 100)