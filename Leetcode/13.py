def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = {}
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        while left < right:
            sum_ = nums[i] + nums[left] + nums[right]
            if sum_ < 0:
                left += 1
            elif sum_ > 0:
                right -= 1
            else:  # sum == 0
                if (nums[i], nums[left], nums[right]) not in result:
                    result[(nums[i], nums[left], nums[right])] = True
                while left + 1 < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right - 1 and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return [list(i) for i in result]


print(threeSum([-1,0,1,2,-1,-4]))