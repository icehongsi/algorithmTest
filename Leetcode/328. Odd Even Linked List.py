# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next = even.next
            even.next = even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return odd
























def solution(head):
    if not head:
        return None
    odd, even = head, head.next
    even_head = head.next
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    odd.next = even.next
    return head