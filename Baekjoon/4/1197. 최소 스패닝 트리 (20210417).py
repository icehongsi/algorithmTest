# 입력받은 edge를 cost순으로 정렬한다

def find(n): #n: node number
    if parents[n] == n: # 부모 노드와 자기 자신이 같은 경우: root node에 도달했을 경우
        return n
    parents[n] = find(parents[n]) # 자신의 부모 노드를 재귀적인 연산을 통해 갱신한다.
    return parents[n]

def union(n, m):
    n, m = find(n), find(m)
    if n > m: #임의로 규칙을 정한다. 더 큰 수가 root에 올 수 있도록 한다.
        parents[m] = n
    else:
        parents[n] = m

def mst():
    ans, connected = 0, 0
    for start, end, weight in edges: # weight에 따라 오름차순으로 정렬된 edge순으로 연산을 수행한다.
        if find(start) != find(end): # union-find 연산을 수행해 부모가 다를 것으로 판명날 경우 합쳐야 한다.
            union(start, end) # 합집합 연산을 통해 합친다.
            ans += weight # 이 경우 weight를 더해준다.
    return ans

v, e = map(int, input().split()) # 정점의 개수, 간선의 개수
parents = list(range(v + 1)) # union-find, i번째 index에 노드 i의 parent가 수록되어 있음
edges = sorted([list(map(int, input().split())) for _ in range(e)], key = lambda x: x[2])
print(mst())
