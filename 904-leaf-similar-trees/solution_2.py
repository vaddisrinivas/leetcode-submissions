# https://leetcode.com/problems/leaf-similar-trees
# https://leetcode.com/problems/904-leaf-similar-trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def cd(node):
            if not (node.left or node.right) : return [node.val]
            lc = cd(node.left) if node.left else []
            rc = cd(node.right) if node.right else []
            # print(lc,rc,node.val)
            return lc + rc 
        lc = cd(root1)
        rc = cd(root2)
        # print(lc,rc)
        return lc==rc
        
        