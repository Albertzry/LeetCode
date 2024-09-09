# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def modify(start,before):
            sum_=0
            current=start.next
            while current.val!=0:
                sum_+=current.val
                current=current.next
            before.next.val=sum_
            before.next.next=current
            return
        before=ListNode()
        before.next=current = head
        while current is not None:
            if current.val==0 and current.next is not None:
                modify(current,before)
            if current.val==0 and current.next is None:
                before.next=None
                break
            current=current.next
            before=before.next
        return head