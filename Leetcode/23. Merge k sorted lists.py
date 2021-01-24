import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = node = ListNode(None)
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))

        while heap:
            tmp = heapq.heappop(heap)
            node.next = ListNode(tmp[0])
            node = node.next
            if lists[tmp[1]].next:  # next node exists
                lists[tmp[1]] = lists[tmp[1]].next
                heapq.heappush(heap, (lists[tmp[1]].val, tmp[1]))

        return root.next





