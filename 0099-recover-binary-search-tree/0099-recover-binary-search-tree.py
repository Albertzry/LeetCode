# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        if root is None:
            return

        def it(node):
            if node is None:
                return
            it(node.left)
            node_val.append(node.val)
            it(node.right)

        def find(node, num):
            if node is None:
                return None
            if node.val == num:
                return node
            left_result = find(node.left, num)
            if left_result:
                return left_result
            return find(node.right, num)

        node_val = []
        it(root)
        minnum = maxnum = None
        for i in range(0, len(node_val)):
            if i>0 and maxnum ==None and node_val[i] < node_val[i - 1]:
                maxnum = node_val[i - 1]
            if i<len(node_val)-1 and node_val[i] > node_val[i + 1]:
                minnum = node_val[i + 1]
        node_max = find(root, maxnum)
        node_min = find(root, minnum)
        if node_max and node_min:
            node_max.val, node_min.val = node_min.val, node_max.val
        return root
        
            



