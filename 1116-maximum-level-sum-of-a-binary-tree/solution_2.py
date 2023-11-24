# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree
# https://leetcode.com/problems/1116-maximum-level-sum-of-a-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue,ms,lms, ps, prev_height = [(root,0)], root.val, 0, 0, 0
        while queue:
            pop, queue = queue.pop(), queue
            if prev_height!=pop[1]:
                if ms<ps:
                    ms = ps
                    lms = prev_height
                ps = 0
            ps += pop[0].val
            prev_height,prev_node = pop[1],pop[0]
            queue = ([(pop[0].left,pop[1]+1)] if pop[0] and pop[0].left else [] )+ queue
            queue = ([(pop[0].right,pop[1]+1)] if pop[0] and pop[0].right else [] )+ queue
        else:
            if ms<ps:
                ms = ps
                lms = prev_height 
        return lms+1