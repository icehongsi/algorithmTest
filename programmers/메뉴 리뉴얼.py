import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        candidates = []
        for order in orders:
            candidates += list(itertools.combinations(order, course_size))

        candidates = collections.Counter(candidates).most_common()
        result += [k for k, v in candidates if v > 1 and v == candidates[0][1]]

    return list(map(lambda x: ''.join(x), result))

def solution(orders, course):
    result = []
    for course_size in course:
        candidates = []
        for order in orders:
            candidates += list(itertools.combinations(sorted(order), course_size))

        candidates = collections.Counter(candidates).most_common()
        result += [k for k, v in candidates if v > 1 and v == candidates[0][1]]

    print(result)
    return sorted(list(map(lambda x: ''.join(x), result)))

solution(["XYZ", "XWY", "WXA"], [2,3,4])
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))