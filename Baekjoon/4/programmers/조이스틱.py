def solution(name):
    name_list = [min(ord("Z") - ord(_) + 1, ord(_) - ord("A")) for _ in name]
    mid, answer = 0, 0
    while True:
        answer += name_list[mid]
        name_list[mid] = 0

        if sum(name_list) == 0:
            return answer

        left, right = 1, 1
        while name_list[(mid - left) % len(name)] == 0:
            left += 1
        while name_list[(mid + right) % len(name)] == 0:
            right += 1

        print(mid, left, right)

        if left >= right:
            answer += right
            mid = (mid + right) % len(name)
        else:
            answer += left
            mid = (mid - left) % len(name)

print(solution("AABAAAAAAAAABBB"))