from collections import deque


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ptr = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[ptr] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
            if nums[ptr] != 0:
                ptr += 1

        """
        Do not return anything, modify nums in-place instead.
        """
