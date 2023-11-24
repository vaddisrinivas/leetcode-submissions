# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree
# https://leetcode.com/problems/1474-longest-zigzag-path-in-a-binary-tree
# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import re
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def cd(node,direction,c):
            
            if not node:
                return c  
            lc = cd(node.left, False, c+1 if direction else 1)
            rc = cd(node.right, True, c+1 if not direction else 1)
            return max(lc,rc)
        return cd(root, None, 0)-1