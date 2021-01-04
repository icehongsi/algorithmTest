'''
206. Reverse Linked List
Easy

5953

116

Add to List

Share
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

def reverseList(head):
    node, prev = head, None # node를 매개변수로 받은 head로, prev를 None로 초기화
    while node:
        next, node.next = node.next, prev #next 변수에 정순 리스트에서의 노드의 다음 노드 저장.
        node, prev = next, node
    return prev

def reverseList(head):
        def rev(node, prev=None):
            if not node: return prev
            node.next, next = prev, node.next
            return rev(next, node)

        return rev(head)