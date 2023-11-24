# https://leetcode.com/problems/count-good-nodes-in-binary-tree
# https://leetcode.com/problems/1544-count-good-nodes-in-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def cd(node,max_num):
            if not (node.left or node.right) : return 1 if node.val>=max_num else 0
            lc = cd(node.left, max(max_num,node.val)) if node.left else 0
            rc = cd(node.right, max(max_num,node.val)) if node.right else 0
            return lc + rc + (1 if node.val>=max_num else 0)
        return cd(root,root.val)