def solution(n, weak, dist):
    diff = []
    for i in range(len(weak)):
        diff.append((weak[(i + 1) % len(weak)] - weak[i]) % n)

    idx = diff.index(max(diff))
    min_idx = (idx + 1) % len(weak)
    max_idx = (idx - 1) % len(weak)
    print(diff)
    print(min_idx, max_idx)
    dist.sort(reverse = True)
    print(dist)
    for idx, value in enumerate(dist):
        print(idx, value)
        while value >= diff[min_idx % len(weak)] and min_idx != max_idx:
            value -= diff[min_idx % len(weak)]
            min_idx = (min_idx + 1) % len(weak)
            print("value: ", value)

        min_idx = (min_idx + 1) % len(weak)

        if min_idx >= max_idx:
            return idx + 1

    return -1








print(solution(12,	[1, 5, 6, 10],	[1, 2, 3, 4]))