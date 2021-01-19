# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node = head
        if not node:
            return False
        while node.next:
            if node.next.val == 10 ** 5 + 1:
                return True
            node.val = 10 ** 5 + 1
            node = node.next
        return False
