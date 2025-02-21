# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.valSet = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.valSet

    def dfs(self, node: TreeNode, val: int):
        if node is None:
            return
        node.val = val
        self.valSet.add(val)
        self.dfs(node.left, val * 2 + 1)
        self.dfs(node.right, val * 2 + 2)

    
# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)