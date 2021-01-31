import time
from collections import deque


def solution(priorities, location):
    queue = []
    for k, v in enumerate(priorities):
        queue.append([v, k]) #value, index
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

    return 0


def solution(priorities, location):
    queue = deque([])
    for k, v in enumerate(priorities):
        queue.append([v, k])
    count = 1
      # 프린터 찾기 O(n)
    priority_order = sorted(priorities)

    while queue:
        priority, idx = queue.popleft()

        if location == idx and priority == priority_order[-1]:
            return count
        elif priority == priority_order[-1]:
            priority_order.pop()
            count += 1
        else:
            queue.append([priority, idx])





print(solution([1, 1, 9, 1, 1, 1], 0))