"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        start = node
        if not start:
            return None
        q = deque([start])
        nodes = {start.val: Node(start.val)}

        while q:
            node = q.popleft()
            for neighbor in node.neighbors:
                if neighbor.val not in nodes:
                    q.append(neighbor)
                    nodes[neighbor.val] = Node(neighbor.val)
                nodes[node.val].neighbors.append(nodes[neighbor.val])

        return nodes[start.val]
