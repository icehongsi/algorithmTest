class Solution:
    def binaryGap(self, n: int) -> int:
        n, point, count, max_amt = bin(n)[2:], 0, 0, 1
        if n.count('1') == 1:
            return 0

        while point < len(n):
            print(n[point], 'count', count, max_amt)
            if n[point] == "1":  # if 1
                if max_amt < count + 1:
                    max_amt = count + 1
                count = 0
            else:  # if 0
                count += 1
            point += 1

        return max_amt