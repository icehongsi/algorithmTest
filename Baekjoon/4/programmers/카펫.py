def solution(brown, yellow):
    for i in range(1, int(brown ** 0.5) + 1):
        if yellow % i == 0:
             if ((i - 1) + (yellow/i - 1)) * 2 + 8 == brown:
                    return [i + 2, int(yellow/i) + 2] if i + 2 >= int(yellow/i) + 2 else [int(yellow/i) + 2, i + 2]
print(solution(10, 2))