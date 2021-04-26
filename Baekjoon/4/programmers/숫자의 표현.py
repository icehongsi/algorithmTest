def solution(n):
    sum_, answer = 0, 0
    plus, minus = 1, 1
    while True:
        while sum_ < n:
            sum_ += plus
            plus += 1

        while sum_ > n:
            sum_ -= minus
            minus += 1

        if sum_ == n:
            answer += 1
            sum_ -= minus
            minus += 1
            if plus == n + 1:
                return answer