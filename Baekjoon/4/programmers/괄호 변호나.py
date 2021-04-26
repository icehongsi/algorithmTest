def isValid(p):
    stack = 0
    if not p:
        return 1
    for i in p:
        if i == "(":
            stack += 1
            continue
        if stack == 0:
            return False
        stack -= 1
    return not bool(stack)


def solution(p):
    # 0. 빈 문자열인지 확인하기
    if not p: return ''
    # 1. 올바른 괄호 문자열인지 확인하기
    if isValid(p): return p
    # 2. 균형잡힌 괄호문자열로 분리하기
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        else:
            right += 1
        if left == right:
            u, v = p[:i + 1], p[i + 1:]
            break

    if isValid(u):
        return u + solution(v)
        '''
        temp = "("
        temp += solution(v)
        temp += ")"
        for p in u[1:len(u) - 1]:
            if p == '(':
                temp += ')'
            else:
                temp += '('

        return temp
        '''

    return "(" + solution(v) + ")" + u[1:len(u) - 1][::-1] if u else "(" + solution(v) + ")"


print(solution("()))((()"))