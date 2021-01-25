# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: #72ms
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        root = node = ListNode(None)
        root.next = head
        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return root.next


class Solution: #84ms
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        root = node = ListNode(None)
        root.next = head

        def removal(node):
            if not node:
                return
            if node.next and node.next.val == val:
                node.next = node.next.next
                removal(node)
            else:
                removal(node.next)

        removal(node)
        return root.next


class Solution: #88ms
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: #끝에 다다랐을 경우
            return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
