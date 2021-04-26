import itertools
def passed(maps):
    for map in maps:
        map = ''.join(map)
        if '0' * K not in map and '1' * K not in map:
            return 0
    return 1


def solve():
    if passed(matrix):
        return 0
    for select in range(1, K): # 덮을 개수
        options = tuple(itertools.product(['0', '1'], repeat = select))
        for combo in tuple(itertools.combinations(range(D), select)):
            check = [x[:] for x in matrix] # 임시 매트릭스
            for option in options:
                for k, v in enumerate(combo):
                    for i in range(W):
                        check[i][v] = option[k]

                if passed(check): return select
    return K

for i in range(int(input())):
    D, W, K = map(int, input().split()) # D: 보호필름 두께 (row), W: 가로 크기 (column), K: 합격 기준
    matrix = [[0] * D for _ in range(W)]
    for c in range(D): # transpose matrix
        temp = input().split()
        for r in range(len(temp)):
            matrix[r][c] = temp[r]

    print(solve())