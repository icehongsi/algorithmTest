
def move(r, c, color_to_avoid, direction):
    move_dir = {
        "east": lambda r, c: (r, c+1),
        "west": lambda r, c: (r, c-1),
        "north": lambda r, c: (r-1, c),
        "south": lambda r, c: (r+1, c)
    }
    while True:
        if map_[r][c] in ("#", "O", color_to_avoid):
            return r, c
        map_[r][c] =
        r, c = move_dir[direction](row, col)

def findWay(r, c, count):
    if [r, c] == o:
        print("SUCCESS!")
        return count
    if c + 1 < col and not visited[r][c+1]:
        if move(r, c)



row, col = list(map(int, input().split()))
map_ = []
# 입력받기
for r in range(row):
    map_.append(input())
    if "B" in map_[-1]:
        b = [row, map_[-1].find("B")]
    if "R" in map_[-1]:
        r = [row, map_[-1].find("R")]
    if "O" in map_[-1]:
        o = [row, map_[-1].find("O")]

visited = [[False for n in range(row)] for _ in range(col)]