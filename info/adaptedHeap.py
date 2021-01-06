class AdapedHeap:
    # Locator 클래스를 여기서 선언 (클래스 안에 다른 클래스 선언 가능)
    def __init__(self):
        self.A = [] # 여기선 빈 리스트로 초기화
    def __str__(self):
        return str(self.A)
    def __len__(self):
        return len(self.A)
    def insert(self, key):
        item = self.Locator(key, len(self.A)) # 마지막 index 삽입
        self.A.append(item) # 힙 리스트에 item 삽입됨!
        self.heapify_up(item.index)
    def heapify_up(self, i): # 인덱스 i에 저장된 item을 up!
        p = (i - 1)//2
        if p > 0 and self[p] < self.A[i]:
        # key swap!
            self.A[i].key, self.A[p].key = self.A[p].key, self.A[i].key
            self.A[i].index = p
            self.A[p].index = i
            self.heapify_up(p)

    def remove(self, loc):  # key 값이 아닌 Locator 객체가 전달됨
        k = loc.index  # self.A[k]에 있는 item을 지우면 됨!

        if not (0 <= k < len(self) and self.A[k] == loc):
        # loc이 힙에 저장된 것이 아니라면 error
            raise ValueError('Invalid locator')
        if k == len(self):  # 맨 마지막 item을 지우는 경우
            self.A.pop()  # 단순히 pop 하면 됨
        else:
        # 1. A[k]와 A[-1]을 swap!
            self.A[k], self.A[-1] = self.A[-1], self.A[k]
            # 2. A[-1]을 pop!
            self.A.pop()
            # 3. A[k]를 heapify_down해서 재 배치
            self.heapify_down(k)