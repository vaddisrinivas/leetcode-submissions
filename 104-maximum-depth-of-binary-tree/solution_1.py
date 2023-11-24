# https://leetcode.com/problems/maximum-depth-of-binary-tree
# https://leetcode.com/problems/104-maximum-depth-of-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def cd(node):
            if not node:
                return 0
            if node.right and node.left:
                return 1+max(cd(node.right),cd(node.left))
            elif node.right and not node.left:
                return 1+cd(node.right)
            elif not node.right and node.left:
                return 1+cd(node.left)
            else:
                return 1
        return cd(root)