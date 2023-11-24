# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
# https://leetcode.com/problems/236-lowest-common-ancestor-of-a-binary-tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        found=[]
        def cd(node,path,target):
            nonlocal found
            if not node:
                return None
            if node.val==target.val:
                # print(path)
                path+=","+str(node.val)
                found.append(path.split(","))
                return node
            # print(path, target.val, node.val)
            lc = cd(node.left,path+","+str(node.val),target) if node.left else None
            rc = cd(node.right,path+","+str(node.val),target) if node.right else None
            return lc if lc else (rc if rc else None)
        prev = None
        t1 = cd(root,"",p)
        t2 = cd(root,"",q)
        t3 = None
        print("**",found)
        if found and len(found)==2:
            for i in range(len(found[0])):  
                if i<len(found[1]) and found[0][i]==found[1][i]:
                    prev = found[0][i]
                else:
                    break
        if prev:
            t3 = cd(root,"",TreeNode(int(prev)))
        return t3