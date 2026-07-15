# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        def insert(value, root):
            if root is None:
                return TreeNode(value)
            if value < root.val:
                root.left = insert(value, root.left)
            else:
                root.right = insert(value, root.right)

            return root
        
        for i in preorder[1:]:
            root = insert(i, root)
        return root