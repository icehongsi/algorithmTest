def subsets(self, nums: List[int]) -> List[List[int]]:
    result = []

    def dfs(index, selected):
        if index >= len(nums):
            return
        for i in range(index, len(nums)):
            result.append(selected + [nums[i]])
            dfs(i + 1, selected + [nums[i]])

    dfs(0, [])

    return result + [[]]

#revised
def subsets(nums):
    result = []
    def dfs(index, selected):
        result.append(selected)
        for i in range(index, len(nums)):
            dfs(i + 1, selected + [nums[i]])

    dfs(0, [])

    return result


print(subsets([1,2,3]))