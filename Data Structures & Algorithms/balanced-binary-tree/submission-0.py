# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = []
        def dfs(node):
            nonlocal stack
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            stack.append(left-right)


            return 1 + max(left, right)
        dfs(root)
        for i in stack:
            if i<=-2 or i>=2:
                return False
        return True

        