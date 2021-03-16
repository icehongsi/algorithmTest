def solution():
    int(input())
    aliquot = sorted(list(map(int, input().split())))

    if len(aliquot) % 2: #제곱수가 있을 경우
        return aliquot[len(aliquot) // 2] ** 2 if len(aliquot) > 2 else aliquot[0] ** 2
    else:
        return min(aliquot) * max(aliquot)

print(solution())