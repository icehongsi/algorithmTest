'''
5. Longest Palindromic Substring
Medium

9066

617

Add to List

Share
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"

해결 방법
'''

def longestPalindrome(s): #return str
    if s == s[::-1] or len(s) == 1:
        return s
    result = [0, 0]

    def augment(start, end):
        while start > 0 and end < len(s) - 1 and s[start-1] == s[end+1]:
            start -= 1
            end += 1
        return [start, end]

    for i in range(len(s)-1):
        if s[i] == s[i+1]: # 단어 두 개로 이루어져있을 경우
            temp = augment(i, i+1) #두 알파벳으로 이루어진 단어를 기준으로 왼쪽 및 오른쪽으로 확장
            if (temp[1] - temp[0]) > (result[1] - result[0]): # 크기 비교 후 새로 발견된 palindrome이 더 클 경우 교체
                result = temp
        if i+2 < len(s) and s[i] == s[i+2]: #단어 세 개로 이루어져있을 경우
            temp = augment(i, i+2) #세 알파벳으로 이루어진 단어를 기준으로 왼쪽 및 오른쪽으로 확장
            if (temp[1] - temp[0]) > (result[1] - result[0]):
                result = temp

    return s[result[0] : result[1]+1]

print(longestPalindrome("abracadabra"))