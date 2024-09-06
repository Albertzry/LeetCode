# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        start = before = ListNode()
        start.next = current = head
        while current is not None:
            if current.val == val:
                before.next=current.next
            else:
                before=before.next
            current=current.next
        return start.next