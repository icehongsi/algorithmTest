def solution(info, query):
    info_dict, answer = [], []
    for k, v in enumerate(info):
        info_dict.append(v.split())

    for q in query:
        count = 0
        temp = q.split(' and ')
        temp.extend(temp.pop().split(' '))

        for info in info_dict:
            count += 1
            for k, v in enumerate(temp):
                if v.isdigit() and int(v) > int(info[k]):
                    count -= 1
                    break
                elif v.isalpha() and v != info[k] and v != "-":
                    count -= 1
                    break

        answer.append(count)

    return answer




solution(
["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
)