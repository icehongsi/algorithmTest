from collections import defaultdict

def solution(gems):
    collection = defaultdict(int)
    n = len(set(gems))
    min_length, answer = len(gems), []
    start, end = 0, 0
    while True:

        while True:
            collection[gems[end]] += 1
            if end == len(gems) - 1 or len(collection) == n: #end가 취할 수 있는 최솟값에 도달한 경우
                break
            end += 1
        while True:
            if collection[gems[start]] == 1: #start가 취할 수 있는 최댓값에 도달한 경우
                break
            collection[gems[start]] -= 1
            start += 1

        if end - start < min_length and len(collection) == n: # start, end의 편차가 최소이며 모든 item을 포함할 경우
            answer = [start + 1, end + 1] # answer 변경
            min_length = end - start

        if end == len(gems) - 1: # end가 끝에 도달한 경우 순회 종료
            return answer

        del collection[gems[start]] # 다음을 찾기 위해 start와 end에 각각 1씩 더하기
        start += 1
        end += 1



solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])