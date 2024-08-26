"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        result=[]
        def bfs(node_list):
            if len(node_list)==0:
                return
            temp=[]
            grandchildren=[]
            for i in range(len(node_list)):
                temp.append(node_list[i].val)
                if node_list[i].children is not None:
                    grandchildren+=node_list[i].children
            result.append(temp[:])                
            bfs(grandchildren)
            return
        if root==None:
            return []
        bfs([root])
        return result
            
               