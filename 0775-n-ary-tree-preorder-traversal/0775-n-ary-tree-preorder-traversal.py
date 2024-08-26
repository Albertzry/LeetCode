"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []

        def ntpt(node):
            if node == None:
                return
            if node.children == None:
                result.append(node.val)
                return
            result.append(node.val)
            for i in range(len(node.children)):
                ntpt(node.children[i])
            return
            
        ntpt(root)
        return result