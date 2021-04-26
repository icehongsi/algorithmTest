import copy
def rotate(maps):
    temp = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            temp[c][N-1-r] = maps[r][c]
    return temp


def move(temp):
    for r in range(N):
        stack, visited = [], [0] * N
        while maps[r]:
            out = maps[r].pop()
            if stack and stack[-1] == out and out > 0 and visited[len(stack)-1] == 0:
                stack[-1] *= 2
            else:
                stack.append(out)
        stack = list(reversed(list(filter(lambda x: x>0, stack))))
        stack += [0] * (N - len(stack))
        temp[r] = stack
    return temp

def solve(n, maps_temp):
    global ans
    temp = copy.deepcopy(maps_temp)
    print(id(temp), temp)

    if n == 5:
        return
    for i in range(4):
        temp = copy.deepcopy(rotate(temp))
        solve(n+1, temp)








N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
ans = 0

solve(0, maps)
print(ans)
'''
for i in temp:
    print(i)
print("-" * 50)'''