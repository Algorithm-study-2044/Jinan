"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        # Start with the root node of the tree
        leftmost = root

        # As long as there is a left child, there are more levels to process
        while leftmost.left:
            # Iterate over the nodes of the current level
            current = leftmost
            while current:
                # Connect the left child to the right child
                current.left.next = current.right

                # Connect the right child to the next left child, if it exists
                if current.next:
                    current.right.next = current.next.left

                # Move to the next node to the right on the current level
                current = current.next

            # Move to the next level, starting with the leftmost node
            leftmost = leftmost.left

        return root
