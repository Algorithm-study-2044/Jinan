"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # A dictionary to save the cloned nodes
        cloned_nodes = {}
        
        def clone(node: 'Node') -> 'Node':
            if node in cloned_nodes:
                return cloned_nodes[node]
            
            # Clone the node
            copy = Node(node.val)
            cloned_nodes[node] = copy
            
            # Clone the neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            
            return copy
        
        return clone(node)