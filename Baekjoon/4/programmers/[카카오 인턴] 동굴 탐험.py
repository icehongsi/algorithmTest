from _collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

def solution(n, path, order):
    prerequisite = {}
    postrequisite = {}
    direction = defaultdict(list)
    for p, q in order:
        prerequisite[q] = p # q 방문 이전에 p를 방문해야 함
    for p, q in path:
        direction[p].append(q)
        direction[q].append(p)
    visited = [False] * n

    def dfs(n):
        if visited[n]: return #이미 방문한 경우 return
        if n in prerequisite and not visited[prerequisite[n]]:
            postrequisite[prerequisite[n]] = n
            return
        visited[n] = True
        if n in postrequisite:
            dfs(postrequisite[n])
        for d in direction[n]:
            dfs(d)

    dfs(0)
    return all(visited)

solution(9, 	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],	[[3, 0]])