from collections import deque


def solution(priorities, location):
    queue = []
    for k, v in enumerate(priorities):
        queue.append([v, k])
    idx, count = 0, 0
    while queue:
        print(queue)
        max_val = max(queue)[0]  # 프린터 찾기 O(n)
        for i in range(idx, idx + len(queue)):
            if queue[i % len(queue)][0] == max_val:
                count += 1
                if queue.pop(i % len(queue))[1] == location:
                    return count
                idx = i % len(queue)
                break

    return None

print(solution([1,1,3,3,5,5], 3))
print(solution([1, 1, 9, 1, 1, 1],0))