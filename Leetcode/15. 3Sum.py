from collections import defaultdict
def threeSum(nums):
    sum_list = defaultdict(list)
    answer_set = []
    ans = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum_list[nums[i] + nums[j]].append((i, j))
    for i in range(len(nums)):
        for a, b in sum_list[-nums[i]]:
            if a != i and b != i and list(sorted([nums[a], nums[b], nums[i]])) not in answer_set:
                answer_set.append(list(sorted([nums[a], nums[b], nums[i]])))
    return answer_set

print(threeSum([-1,0,1,2,-1,-4]))