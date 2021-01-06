def solution(tickets):
    direction = {}
    city = {"ICN": True}
    for ticket in tickets:
        if ticket[0] in direction:
            direction[ticket[0]].append(ticket[1])
        else:
            direction[ticket[0]] = [ticket[1]]

    init = direction["ICN"]

    for i in direction:
        print(i)




    answer = []
    return answer

solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])