# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
     
        def bfs(node_set):
            temp = []
            res = 0
            for node in node_set:
                res+=node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            ans.append(res)
            if not temp:
                return
            bfs(temp)
              
        ans=[]
        bfs([root])
        ans = sorted(ans,reverse=True)
        return ans[k-1] if k <=len(ans) else -1
            