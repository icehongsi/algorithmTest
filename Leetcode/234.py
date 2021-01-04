def isPalindrome(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result == result[::-1]