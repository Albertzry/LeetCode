# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def pt(node):
            if node == None:
                return
            pt(node.left)
            pt(node.right)
            result.append(node.val)
            return
        pt(root)
        return result
