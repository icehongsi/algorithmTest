def dailyTemperatures(T):
    stack = []
    wait = [0] * len(T)
    for idx, temp in enumerate(T):
        count = 0
        while stack and T[stack[-1]] < temp:
             popped = stack.pop()
             wait[popped] = (idx - popped)
        stack.append(idx)
    return wait

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))