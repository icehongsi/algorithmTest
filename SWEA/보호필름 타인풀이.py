import itertools

def inspect(film):
    for L in film:
        layer = ''.join(L)
        if '1'*K not in layer and '0'*K not in layer:
            return 0
    return 1


def inject(film):
    for i in range(1, D+1):
        # 열 선택
        tries = itertools.combinations(tuple(range(D)), i)
        # 열에 넣을 약품 선택
        combs = tuple(itertools.product(['0', '1'], repeat=i))

        for tri in tries:
            filmtemp = [ layer[:] for layer in film ]
            for comb in combs:
                for l, row in enumerate(tri):
                    for m in range(W):
                        filmtemp[m][row] = comb[l]
                if inspect(filmtemp):
                    print(comb)
                    return i
    return -1


T = int(input())
# for test_case in [1]:
for test_case in range(1, T + 1):
    maxi = 0
    D, W, K = map(int, input().split())

    arr = [[0]*D for _ in range(W)]
    for i in range(D):
        eles = input().split()
        for j in range(W):
            arr[j][i] = eles[j]
    # arr = list(map(list, zip(*arr)))

    if inspect(arr):
        maxi = 0
    else:
        maxi = inject(arr)

    print("#%d %d" % (test_case, maxi))