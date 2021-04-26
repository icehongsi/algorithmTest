'''
def multiply(idx, value):
    global answer
    if idx == len(apparel_list):
        answer += value
        return
    multiply(idx + 1, value * apparels[apparel_list[idx]])
    multiply(idx + 1, value)

multiply(0, 1)


for i in range(1, len(apparels) + 1):
    for j in combinations(apparels.keys(), i):
        temp = 1
        for k in j:
            temp *= apparels[k]
        answer += reduce(lambda x, y: x * y, apparels[j])
'''