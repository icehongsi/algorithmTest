from collections import defaultdict
def findItinerary(tickets):
    graph = defaultdict(list)
    for i, j in sorted(tickets):
        graph[i].append(j)
    route = []
    def dfs(city):
        print(graph)
        while graph[city]:
            dfs(graph[city].pop(0))
        route.append(city)


    dfs("JFK")

    return route[::-1]

findItinerary([['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']])
findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])