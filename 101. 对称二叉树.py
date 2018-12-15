# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.ret(root.left,root.right)
        else:
            return True
        
    def ret(self,p,q):
        if p and q:
            return p.val == q.val and self.ret(p.left,q.right) and self.ret(p.right,q.left)
        else:
            return not p and not q
            