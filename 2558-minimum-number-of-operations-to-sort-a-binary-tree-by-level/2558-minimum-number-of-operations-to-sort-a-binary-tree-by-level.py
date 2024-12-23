# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans, q = 0, [root]
        while q:
            a = []
            tmp = q
            q = []
            for node in tmp:
                a.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            n = len(a)
            a = sorted(range(n), key=lambda i: a[i])

            ans += n
            vis = [False] * n
            for v in a:
                if vis[v]: continue
                while not vis[v]:
                    vis[v] = True
                    v = a[v]
                ans -= 1
        return ans
