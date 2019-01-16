class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxLevel = 1
        self.val = root.val
        self.helper(root, 1)
        return self.val

    def helper(self, root, level):
        if not root:
            return
        if level > self.maxLevel:
            self.maxLevel = level
            self.val = root.val

        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)