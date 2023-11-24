# https://leetcode.com/problems/search-in-a-binary-search-tree
# https://leetcode.com/problems/783-search-in-a-binary-search-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def s(node,val):
            if not node:
                return
            if node.val==val:
                return node
            elif node.val>val:
                return s(node.left,val)
            else:
                return s(node.right,val)
        return s(root,val)