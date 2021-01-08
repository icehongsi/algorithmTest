def permute(nums):
    result = []
    elem = []
    def permute_recursive(nums):
        if not nums:
            result.append(elem[:])
        for i in nums:
            temp = nums[:]
            temp.remove(i)
            elem.append(i)
            permute_recursive(temp)
            elem.pop()

    permute_recursive(nums)
    print(result)


nums = [1,2,3]

permute(nums)