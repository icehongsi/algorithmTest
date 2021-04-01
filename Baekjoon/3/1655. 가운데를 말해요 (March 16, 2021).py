import heapq
#heapq ... 0번째 인덱스는 최솟값 저장
def solution():
    lower, upper = [], []
    median = []
    for i in range(int(input())): # 반복 횟수 입력
        num = int(input())

        if i % 2: #홀수일 경우
            heapq.heappush(upper, num)
        else: #짝수일 경우
            heapq.heappush(lower, -num)

        if upper and -lower[0] > upper[0]: #만약 최소힙의 최댓값이 최대힙의 최솟값보다 클 경우
            low, high = heapq.heappop(lower), heapq.heappop(upper) # 최소힙과 최대힙간 head 교체
            heapq.heappush(lower, -high)
            heapq.heappush(upper, -low)

        median.append(-lower[0]) #항상 최소힙의 head가 중앙값이 됨

    print("\n".join(map(str, median)))

solution()