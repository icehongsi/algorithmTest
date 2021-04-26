from collections import defaultdict


def solution(tickets):
    global result
    result = []
    answer, cities = [], defaultdict(list)
    for i in tickets:
        cities[i[0]].append(i[1])
    for i in cities:
        cities[i].sort()

    visited = dict(zip(list(map(lambda x: tuple(x), tickets)), [False] * len(tickets)))

    def dfs(iternary):
        if len(iternary) == len(tickets) + 1:
            return iternary

        for i in cities[iternary[-1]]:
            if not visited[(iternary[-1], i)]:
                visited[(iternary[-1], i)] = True
                iternary.append(i)
                ret = dfs(iternary)
                if ret:
                    return ret
                visited[(iternary[-1], i)] = False
                iternary.pop()
    print(result)
    #return dfs(["ICN"])


solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])