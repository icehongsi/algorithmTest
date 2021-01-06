class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        node = head
        while node and node.next:
            temp = node.next
            node.next = temp.next
            temp.next = node
            prev.next = temp
            node = node.next
            prev = prev.next.next
        return root.next




def swapPairs(head):
    while head and head.next:
        temp = head.next
        head.next= swapPairs(temp.next)
        temp.next = head
        return temp
    return head

def swapPairs(head):
    root = node = ListNode(None)
    root.next = head

    def swap(node):
        if not (node and node.next):
            return node
        temp = node.next
        node.next = temp.next
        return temp

    while node:
        node.next = swap(node.next)
        node = node.next.next

    return root.next