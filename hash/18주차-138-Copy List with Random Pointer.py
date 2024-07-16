"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Step 1: Clone nodes and insert them next to original nodes
        current = head
        while current:
            new_node = Node(current.val, current.next)
            current.next = new_node
            current = new_node.next

        # Step 2: Assign random pointers for the cloned nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the cloned list from the original list
        current = head
        cloned_head = head.next
        while current:
            cloned_node = current.next
            current.next = cloned_node.next
            if cloned_node.next:
                cloned_node.next = cloned_node.next.next
            current = current.next

        return cloned_head
