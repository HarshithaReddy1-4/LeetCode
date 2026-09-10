# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        def elements(root):
            if root is None:
                return 0
            l = elements(root.left)
            r = elements(root.right)
            return 1 + l + r
        
        def f(root):
            nonlocal count
            if root is None:
                return 0
            l = f(root.left)
            r = f(root.right)
            n = elements(root)
            if ((root.val + l + r)//n) == root.val:
                count += 1
            return root.val + l + r

        f(root)
        return count