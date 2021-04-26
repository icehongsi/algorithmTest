from collections import deque
def solve():
    n, k = map(int, input().split())
    sp = n // 4
    number = input()
    comp = number
    unique_numbers = set()
    while True:
        number = number[1:] + number[0]
        if number == comp:
            return sorted(list(unique_numbers), reverse = True)[k-1]
        for i in range(0, len(number), sp):
            unique_numbers.add(int(number[i:i+sp], 16))


T = int(input())
answer = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f"#{test_case} {solve()}")
