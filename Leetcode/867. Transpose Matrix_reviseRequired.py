
#내가 푼 답
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return list(zip(*A))