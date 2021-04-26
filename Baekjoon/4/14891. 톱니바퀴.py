from collections import deque
def solve():
    magnet = [deque(map(int, list(input()))) for _ in range(4)]
    for _ in range(int(input())):
        n, d = map(int, input().split())
        n -= 1
        move = [0] * 4; move[n] = d

        for i in range(n, 3):
            if magnet[i][2] ^ magnet[i+1][6]:
                move[i+1] = move[i] * -1
            else: break
        for i in range(n, 0, -1):
            if magnet[i][6] ^ magnet[i-1][2]:
                move[i-1] = move[i] * -1
            else: break

        for i in range(4):
            if move[i]:
                magnet[i].rotate(move[i])
    return sum(magnet[i][0] * (2**i) for i in range(4))
print(solve())