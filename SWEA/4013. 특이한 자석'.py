from collections import deque
def solve():
    magnet = [deque(list(map(int, input().split()))) for _ in range(4)]
    K = int(input())
    move = [list(map(int, input().split())) for _ in range(K)]
    score = [1, 2, 4, 8]
    for num, direction in move:
        num -= 1
        move_dir = [0] * 4; move_dir[num] = direction
        dir = direction
        indicator = 2
        for i in range(num, 3):
            if magnet[i][indicator] == magnet[i+1][8 - indicator]:
                break
            dir = dir * -1
            move_dir[i+1] = dir
        indicator = 6
        dir = direction
        for i in range(num, 0, -1):
            if magnet[i][indicator] == magnet[i-1][8-indicator]:
                break
            dir = dir * -1
            move_dir[i-1] = dir
        for k, v in enumerate(move_dir):
            if v == 1:
                magnet[k].appendleft(magnet[k].pop())
            elif v == -1:
                magnet[k].append(magnet[k].popleft())
    ans = 0
    for k, v in enumerate(magnet):
        ans += score[k] * v[0]

    return ans

print(solve())