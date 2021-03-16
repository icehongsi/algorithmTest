def solution():
    R, G, B = 0, 0, 0
    for i in range(int(input())):
        r, g, b = map(int, input().split())

        r_temp = min(G + r, B + r)
        g_temp = min(B + g, R + g)
        b_temp = min(R + b, G + b)

        R, G, B = r_temp, g_temp, b_temp #비교가 끝났으면 R, G, B에 각 변수를 새롭게 할당


    print(min(R, G, B))

solution()