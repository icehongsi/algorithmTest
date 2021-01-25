def solution(n):
    answer = [[None] * i for i in range(1, n + 1)]
    answer[0][0] = 1
    r, c, num, flag = 0, 0, 1, 0
    for i in range(n, -1, -1):
        #print(answer, r, c)
        if flag == 0:  # going down
            #print("down")
            for j in range(i):
                answer[r + j][c] = num
                num += 1
            r, c = r + j, c + 1
        elif flag == 1:  # going right
            #print("right")
            for j in range(i):
                answer[r][c + j] = num
                num += 1
            r, c = r - 1, c + j - 1
        else:
            #print("up")
            for j in range(i):
                answer[r - j][c - j] = num
                num += 1
            r, c = r - j + 1, c - j

        flag = (flag + 1) % 3

    result = []
    for i in answer:
        result.extend(i)
    return result


solution(6)