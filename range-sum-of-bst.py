class Solution(object):
    def rangeSumBST(self, root, L, R):


        sum=0
        if not root:
            return sum
        if L<=root.val<=R:
            sum+=root.val
        if L<=root.val:
            sum+=self.rangeSumBST(root.left,L,R)
        if R > root.val:
            sum+=self.rangeSumBST(root.right,L,R)
        return sum



class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
if __name__=="__main__":
    root=TreeNode(10)

    root.left=5
    root.left.left=3
    root.left.right=7

    root.right=15
    root.right.right=18
    print(Solution.rangeSumBST(root,7,10))