def solution():
    n, l, w, h = map(int, input().split())

    left, right = 0, max(l, w, h)


    for i in range(10000):
        value = (left + right) / 2
        if (l // value) * (w // value) * (h // value) >= n:
            left = value
        else:
            right = value

    print("%.10f" % value)
    #print(((value * (10**9)) // 1) / (10**9))

solution()