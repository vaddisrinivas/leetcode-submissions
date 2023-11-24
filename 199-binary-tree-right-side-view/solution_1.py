# https://leetcode.com/problems/binary-tree-right-side-view
# https://leetcode.com/problems/199-binary-tree-right-side-view
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        queue.append((root,0))
        prev_height = 0
        prev_node = None
        to_print = []
        while queue:
            pop, queue = queue[-1], queue[:-1]
            if prev_height!=pop[1]:
                to_print += [prev_node.val]
            prev_height,prev_node = pop[1],pop[0]
            queue = ([(pop[0].left,pop[1]+1)] if pop[0] and pop[0].left else [] )+ queue
            queue = ([(pop[0].right,pop[1]+1)] if pop[0] and pop[0].right else [] )+ queue
        else:
            if prev_node:
                to_print += [prev_node.val]
        return to_print