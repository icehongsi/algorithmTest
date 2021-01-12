def solution(stones, k):
    answer = 200000001
    index = 0
    while index + k <= len(stones):
        max_val = max(stones[index:index+k])
        if max_val < answer:
            answer = max_val
        index = index + stones[index:index+k].index(max_val) + 1

    return answer


print(solution([200000000,200000000,200000000,200000000,200000000,200000000], 3))