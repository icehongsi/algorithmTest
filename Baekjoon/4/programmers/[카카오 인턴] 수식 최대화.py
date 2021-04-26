from itertools import permutations
import re


def solution(expression):
    answer = 0

    def calculate(int2, int1, operator):
        int1, int2 = int(int1), int(int2)
        if operator == "+":
            return int1 + int2
        elif operator == "-":
            return int1 - int2
        else:
            return int1 * int2

    expression = re.compile("(\D)").split(expression)
    for p, q, r in permutations(["+", "-", "*"], 3):
        order = {p:0, q:1, r:2}
        operand, operator = [], []
        for e in expression:
            if e.isdigit():
                operand.append(e)
            else:
                while operator and order[e] >= order[operator[-1]]:
                    operand.append(calculate(operand.pop(), operand.pop(), operator.pop()))
                operator.append(e)
        while operator:
            operand.append(calculate(operand.pop(), operand.pop(), operator.pop()))
        answer = max(abs(operand[0]), answer)

    return answer

print(solution("100-200*300-500+20"))