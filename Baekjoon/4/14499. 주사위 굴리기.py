


def solve(): #dice 좌표
    dice = [0,0,0,0,0,0] #upper, north, south, east, west, floor (not accessible)
    d = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
    row, col, r, c, k = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(row)]
    order = list(map(int, input().split()))

    def roll(r, c, d, direction):  # 1: 동, 2: 서, 3: 남, 4: 북
        if direction == 1:  # 동쪽
            d = [d[3], d[1], d[0], d[5], d[4], d[2]]
            r, c = r, c + 1
        elif direction == 2:  # 서쪽
            d = [d[2], d[1], d[5], d[0], d[4], d[3]]
            r, c = r, c - 1
        elif direction == 3:  # 북쪽
            d = [d[4], d[0], d[2], d[3], d[5], d[1]]
            r, c = r - 1, c
        else:  # 남쪽
            d = [d[1], d[5], d[2], d[3], d[0], d[4]]
            r, c = r + 1, c

        return r, c, d

    for o in order:
        dr, dc = d[o]
        if not (0 <= r+dr < row or 0 <= c+dc < col):
            continue
        r, c, dice = roll(r, c, dice, o)
        print(dice[0])
        if map_[r][c] == 0:
            map_[r][c] = dice[-1]

        else: #0이 아닌 경우
            dice[-1] = map_[r][c]
            map_[r][c] = 0



solve()

'''
def solve(r, c): #dice 좌표
    dice = [0,0,0,0,0,0] #upper, north, south, east, west, floor (not accessible)
    d = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
    def roll(r, c, d, direction): #1: 동, 2: 서, 3: 남, 4: 북
        if direction == 1: # 동쪽
            d = [d[3],d[1],d[0],d[5],d[4],d[2]]
            r, c = r, c+1
        elif direction == 2: # 서쪽
            d = [d[2],d[1],d[5],d[0],d[4],d[3]]
            r, c = r, c-1
        elif direction == 3: # 북쪽
            d = [d[4],d[0],d[2],d[3],d[5],d[1]]
            r, c = r-1, c
        else: # 남쪽
            d = [d[1],d[5],d[2],d[3],d[0],d[4]]
            r, c = r+1, c

        return r, c, d

    for o in order:
        dr, dc = d[o]
        if 0 <= r+dr < row and 0 <= c+dc < col:
            r, c, dice = roll(r, c, dice, o)
            print(dice[0])
            if map_[r][c] == 0:
                map_[r][c] = dice[-1]

            else: #0이 아닌 경우
                dice[-1] = map_[r][c]
                map_[r][c] = 0


row, col, r, c, k = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(row)]
order = list(map(int, input().split()))
solve(r, c)
'''