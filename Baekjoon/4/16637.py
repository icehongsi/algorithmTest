def calculator(int1, operator, int2):
    if operator == "*":
        return int1 * int2
    elif operator == "-":
        return int1 - int2
    elif operator == "+":
        return int1 + int2

def calculate(appended): #formula를 받아 정답을 출력시키는 함수
    while len(appended) > 1:
        appended.insert(0, calculator(appended.pop(0), appended.pop(0), appended.pop(0)))
    return sum(appended)

def solve(appended, idx):

    global max_value
    if idx >= n:
        max_value = max(max_value, calculate(appended))
        return
    if formula[idx].isdigit(): #해당 index에 위치한 것이 숫자일 경우
        solve(appended + [int(formula[idx])], idx + 1)
    else:
        #1. 추가하지 않고 그냥 넘어가기
        solve(appended + [formula[idx]], idx + 1)
        #2. 현재 부분에 대해 괄호를 친 값을 따로 삽입하고 넘어가기
        appended.append(calculator(appended.pop(), formula[idx], int(formula[idx + 1])))
        solve([calculate(appended)], idx + 2)


n = int(input())
formula = list(input())
max_value = -2<<31
solve([], 0)
print(max_value)