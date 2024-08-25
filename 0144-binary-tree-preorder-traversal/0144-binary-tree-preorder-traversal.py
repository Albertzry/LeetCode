# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def pt(node):
            if node == None:
                return
            result.append(node.val)
            pt(node.left)        
            pt(node.right)
            return
        pt(root)
        return result