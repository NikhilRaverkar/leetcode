# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        return self.helper(root)

    def helper(self, root):
        if not root:
            return None

        root.left = self.helper(root.left)
        root.right = self.helper(root.right)

        if not root.left and not root.right and root.val == 0:
            return None

        return root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
