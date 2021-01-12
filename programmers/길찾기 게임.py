from sys import maxsize

class Node:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def solution(nodeinfo):
    nodeinfo = sorted(nodeinfo, key = lambda x: x[0], reverse = True)
    max_y = nodeinfo[0][0]


