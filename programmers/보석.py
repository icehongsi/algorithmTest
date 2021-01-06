import sys
import heapq

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

def solution(gems):
    size = len(set(gems))
    result = [0, len(gems) - 1]
    check = {gems[0]: 1}
    left, right = 0, 0
    while right < len(gems) and left < len(gems):
        if size == len(check):
            if result[1] - result[0] > right - left:
                result = [left, right]
            if check[gems[left]] == 1:
                del check[gems[left]]
            else:
                check[gems[left]] -= 1

            left += 1


        else:
            right += 1
            if right == len(gems): break
            if gems[right] not in check:
                check[gems[right]] = 1
            else:
                check[gems[right]] += 1

    return [result[0] + 1, result[1] + 1]



print(solution(gems))