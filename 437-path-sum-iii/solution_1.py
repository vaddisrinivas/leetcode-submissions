# https://leetcode.com/problems/path-sum-iii
# https://leetcode.com/problems/437-path-sum-iii
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def cd(node, visited):  
            if not node:
                return 0
            c = 0
            for i,j in enumerate(visited):
                visited[i] = j + node.val
                if visited[i]==targetSum:
                    c += 1
            
            visited += [node.val]
            if visited[-1]==targetSum:
                c += 1
            lc = cd(node.left, visited.copy()) if node.left else 0
            rc = cd(node.right, visited.copy()) if node.right else 0
            return c + rc + lc
        if not root:
            return 0
    
        return cd(root, [])