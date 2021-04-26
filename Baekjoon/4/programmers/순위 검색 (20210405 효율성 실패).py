from collections import defaultdict


def solution(info, query):
    # 1. data 전처리
    infos = defaultdict(list)
    score = 0
    case = [1] * 4
    temp = []
    answer = []

    def cases(idx, string = ''):
        if idx == len(case):
            infos[string].append(score)
            return
        cases(idx + 1, string + temp[idx])
        cases(idx + 1, string + "-")

    for i in info:
        temp = i.split()
        score = int(temp[-1])
        cases(0)

    for k in infos.values():
        k.sort()

    for q in query:
        temp = q.split()
        score = int(temp[-1])
        temp = "".join(temp[:-1]).replace("and", "")
        temp = infos[temp]
        start, end = 0, len(temp)
        while start != end and start != len(temp):
            if temp[(start + end) // 2] >= score:
                end = (start + end) // 2
            else:
                start = (start + end) // 2 + 1
        answer.append(len(temp) - start)
    return answer


solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])