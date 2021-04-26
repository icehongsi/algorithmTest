def solution(numbers, hand):
    phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    lr, lc, rr, rc = 3, 0, 3, 2
    answer = ''

    for i in numbers:
        for r in range(4):
            for c in range(3):
                if phone[r][c] == int(i):
                    if c == 0:  # L
                        answer += 'L'
                        lr, lc = r, c
                    elif c == 2:  # R
                        answer += 'R'
                        rr, rc = r, c
                    elif c == 1:  # M
                        tl, tr = abs(lr - r) + abs(lc - c), abs(rr - r) + abs(rc - c)
                        if tl == tr:
                            if hand == "left":
                                answer += 'L'
                                lr, lc = r, c
                            elif hand == "right":
                                answer += 'R'
                                rr, rc = r, c
                        elif tl > tr:
                            answer += 'R'
                            rr, rc = r, c

                        else:
                            answer += 'L'
                            lr, lc = r, c

    return answer


print(solution(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"
))