def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        compressed, string, iter = '', s[:i], 1
        start, end = i, (2 * i)
        while end <= len(s):
            if string == s[start:end]:
                iter += 1
            else:
                if iter == 1:
                    compressed += string
                else:
                    compressed += str(iter) + string
                string = s[start:end]
                iter = 1
            start, end = end, end + i
        if iter == 1:
            compressed += string + s[start:]
        else:
            compressed += str(iter) + string + s[start:]
        answer = min(answer, len(compressed))
    return answer


solution("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")