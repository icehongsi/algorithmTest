# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # designate m
        root = start = ListNode(None)
        root.next = head
        for i in range(m - 1):
            start = start.next
        end = start.next

        for i in range(n - m):
            temp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = temp

        return root.next








