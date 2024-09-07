# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(head,cur,root):
            if cur is None:  
                return True
            if root is None:  
                return False
            if cur.val == root.val:
                cur = cur.next  
            elif head.val == root.val:
                head = head.next  
            else:
                cur = head  
            return dfs(head, cur, root.left) or dfs(head, cur, root.right)
        return dfs(head,head,root)