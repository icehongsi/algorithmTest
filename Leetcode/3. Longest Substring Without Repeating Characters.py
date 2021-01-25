from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            if len(s) == 0: return 0
            alphabet = {}
            max_length = start = 0
            for i, v in enumerate(s):
                if v in alphabet and start <= alphabet[v]: # when the alphabet is already used and 'start' variable is equal or smaller than alphabet[v]
                    start = alphabet[v] + 1 #alphabet[v] + 1 will be a new start
                else:
                    if max_length < i-start+1:
                        max_length = i-start+1 #adjust maximum length
                alphabet[v] = i #assign new index
            return max_length



def lengthOfLongestSubstring(s):
        start, end, max_value = 0, 0, 0
        freq = {}
        while start <= end < len(s):
            if s[end] not in freq or freq[s[end]] == 0:  # 새로운 문자일 경우
                freq[s[end]] = 1  # hash에 추가
                end += 1
                max_value = max_value if max_value > (end - start) else (end - start)
            else:
                freq[s[start]] -= 1
                start += 1
        return max_value



lengthOfLongestSubstring('bbbbb')