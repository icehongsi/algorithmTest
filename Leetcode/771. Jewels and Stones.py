from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = Counter(stones)
        return sum(stones[i] for i in jewels)