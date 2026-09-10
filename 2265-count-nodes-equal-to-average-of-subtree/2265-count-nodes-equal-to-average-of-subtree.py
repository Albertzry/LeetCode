# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        rc = []

        def dfs(node):
            v = node.val
            c = 1
            if node.left:
                vt,ct=dfs(node.left)
                v+=vt
                c+=ct
            if node.right:
                vt,ct=dfs(node.right)
                v+=vt
                c+=ct
            rc.append([node.val,v,c])
            return v,c   
        
        dfs(root)
        ans=0
        for pair in rc:
            if pair[0] == pair[1]//pair[2]:
                ans+=1
        return ans
            
        
         
