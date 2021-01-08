def solution(routes):
    routes.sort(key=lambda x: x[1])
    min_value = -30001
    answer = 0
    for route in routes:
        if route[0] > min_value:
            min_value = route[1]
            answer += 1
    return answer



solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])