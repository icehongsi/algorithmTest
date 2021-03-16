def removeDuplicates(nums):
    before, count = -10001, 0
    for i in range(len(nums)):
        if nums[i] == before:
            continue
        else:
            before = nums[i]
            count += 1
    return count

print(removeDuplicates([1,1,2]))