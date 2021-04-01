def solution(n):
    if n < 3:
        return [0, 1, 2][n]

    prev, curr = 1, 2

    for i in range(3, n+1):
        temp = (prev + curr) % 15746
        prev, curr = curr, temp


    return curr


print(solution(1000000))