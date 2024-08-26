# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result=[]
        def bfs(node_list):
            if not node_list:
                return
            temp=[]
            grandchildren=[]
            for i in range(len(node_list)):
                temp.append(node_list[i].val)
                if node_list[i].left:
                    grandchildren.append(node_list[i].left)
                if node_list[i].right:
                    grandchildren.append(node_list[i].right)
            result.append(temp[:])
            bfs(grandchildren)
            return
        if not root:
            return result
        bfs([root])
        return result
                