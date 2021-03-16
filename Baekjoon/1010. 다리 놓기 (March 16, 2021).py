def combination(a, b):
    def product(a, b):
        answer = 1
        for i in range(b):
            answer *= (a - i)
        return answer

    return int(product(a, b) / product(b, b))

def solution():
    answer = []
    for i in range(int(input())):
        a, b = map(int, input().split())
        answer.append(combination(a, b) if a > b else combination(b, a))

    print("\n".join(map(str, answer)))

solution()