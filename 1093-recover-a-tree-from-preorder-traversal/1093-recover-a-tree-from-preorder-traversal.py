# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        path, pos = list(), 0
        while pos < len(traversal):
            level = 0
            while traversal[pos] == '-':
                level += 1
                pos += 1
            value = 0
            while pos < len(traversal) and traversal[pos].isdigit():
                value = value * 10 + (ord(traversal[pos]) - ord('0'))
                pos += 1
            node = TreeNode(value)
            if level == len(path):
                if path:
                    path[-1].left = node
            else:
                path = path[:level]
                path[-1].right = node
            path.append(node)
        return path[0]
