class Solution:
    def numIslands(self, grid) -> int:
        count = 0

        def dfs(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] != "1":
                return
            grid[i][j] = 0
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j - 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1
        return count


def numIslands(grid):
    def dfs(row, col):
        if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0 or grid[row][col] == "0":
            return True # 행, 열이 범위를 벗어났거나 육지가 아닐 경우 return
        grid[row][col] = "0" # 0으로 바꾸기
        dfs(row+1, col) # 동서남북 방향에 대해 재귀적으로 실행
        dfs(row-1, col)
        dfs(row, col+1)
        dfs(row, col-1)

    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "1": #육지를 발견했을 경우 dfs 실행
                dfs(row, col)
                count += 1 # return될 경우 섬 개수에 1 더하기

    return count


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid))