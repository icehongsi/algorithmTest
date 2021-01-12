from collections import deque
def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i in range(len(prices)):
        if stack and prices[stack[-1]] > prices[i]: #stack이 비어있거나,
            while stack and prices[stack[-1]] > prices[i]:
                temp = stack.pop()
                answer[temp] = (i - temp)
        stack.append(i)

    while stack:
        n = len(prices) - 1
        temp = stack.pop()
        answer[temp] = (n - temp)

    return answer


print(solution([1,1,1,1,1]))