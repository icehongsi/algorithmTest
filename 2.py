import sys

#sys.stdin = open("input.txt", "r")

from collections import deque


def solution():
    global processor
    # 1. 코어의 좌표 구하기
    cores = []
    result = []
    for i in range(n):
        for j in range(n):
            if processor[i][j] == 1 and 0 < i < n - 1 and 0 < j < n - 1:
                cores.append([j, i-1])
    print(cores)

    # 2. 코어에 대한 동서남북 연산
    def backtracking(idx=0, connected_core=0, count=0):  # idx
        global processor
        if idx == len(cores):
            print(idx, connected_core, count, "끝까지 달성")

            for i in processor:
                print(i)
            print("-" * 100)

            result.append([connected_core, count])
            return


        flag = False
        processor_saved = processor[:]
        r, c = cores[idx]

        print(r, c, connected_core, count)



        print(r, c)


        print("동")
        for i in range(c + 1, len(processor) + 1):  # 동쪽
            if i == len(processor):
                flag = True
                backtracking(idx + 1, connected_core + 1, count + (i - c - 1))
            elif processor[r][i] == 1:
                break
            else:
                processor[r][i] = 1  # 1로 마크

        processor = processor_saved[:]

        print(r, c)

        print("서")
        for i in range(c - 1, -2, -1):  # 서쪽
            if i == -1:
                flag = True
                backtracking(idx + 1, connected_core + 1, count + (c - i - 1))
            elif processor[r][i] == 1:
                break
            else:
                processor[r][i] = 1  # 1로 마크

        processor = processor_saved[:]

        print(r, c)

        print("북")

        for i in range(r - 1, -2, -1):  # 북쪽
            if i == -1:
                flag = True
                backtracking(idx + 1, connected_core + 1, count + (r - i - 1))
            elif processor[i][c] == 1:
                break

            else:
                processor[i][c] = 1


        processor = processor_saved[:]

        print(r, c)

        print("남")

        for i in range(r + 1, len(processor) + 1):
            if i == len(processor):
                flag = True
                backtracking(idx + 1, connected_core + 1, count + (i - r - 1))
            elif processor[i][c] == 1:
                break
            else:
                processor[i][c] = 1

        processor = processor_saved[:]

        if not flag:
            backtracking(idx + 1, connected_core, count)

    backtracking()
    print(sorted(result))

# 동, 서, 남, 북에 대해 체크하기


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    processor = [list(map(int, input().split())) for _ in range(n)]
    solution()