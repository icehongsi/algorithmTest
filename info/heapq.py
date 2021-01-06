class Node:
    def __init__(self, val = None):
        self.val = val


heap = []
heap.append(Node(1))
heap.append(Node(2))

import heapq
heapq.heapify(heap)