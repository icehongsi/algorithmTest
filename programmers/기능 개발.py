import time
from math import ceil
def solution(progresses, speeds):
    remained = [ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    answer, elapsed, count = [], remained[0], 0
    for i in range(1, len(remained)):
        count += 1
        if remained[i] > elapsed:
            elapsed = remained[i]
            answer.append(count)
            count = 0

    answer.append(count + 1)
    print(answer)

solution( [95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1])
solution( [93, 30, 55],[1, 30, 5])