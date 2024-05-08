# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def max_gain(node):
            if not node:
                return 0

            # Recursively get the maximum gain from left and right subtrees
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # New path price to be considered including this node
            local_path_sum = node.val + left_gain + right_gain

            # Update the maximum path sum encountered
            self.max_sum = max(self.max_sum, local_path_sum)

            # Return the maximum gain if continuing the same path
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum
