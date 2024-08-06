# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    empty = '#'

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        s = [root]
        l = []

        while s:
            node = s.pop()
            if not node:
                l.append(self.empty)
            else:
                l.append(str(node.val))
                s.append(node.left)
                s.append(node.right)
        
        return ','.join(l)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []

        global i
        i = 0
        
        l = data.split(',')
        print(l)
        return self.helper(l)
    
    def helper(self, l):
        global i
        if l[i] == self.empty:
            return None

        root = TreeNode(l[i])
        i += 1
        root.right = self.helper(l)
        i += 1
        root.left = self.helper(l)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))