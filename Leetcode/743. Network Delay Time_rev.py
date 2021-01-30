from collections import defaultdict
import heapq
def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for source, target, time in times: # 1. add all edges into dictionary
        graph[source].append((target, time))
    queue = [(0, k)]
    dist = defaultdict(int)
    while queue:
        time, node = heapq.heappop(queue) # 최소의 시간을 가진 값 출력
        if node not in dist: #node가 거쳐간 시간이 측정되지 않았을 경우
            dist[node] = time # 시간 기록
            for v, w in graph[node]: # 다음으로 순회할 모든 원소들에 대해서
                heapq.heappush(queue, (time + w, v))

    if len(dist) == n:
        return max(dist.values())
    return -1






times = [[2,1,1],[2,3,1],[3,4,1]]; n = 4; k = 2

networkDelayTime(times, n, k)