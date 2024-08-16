# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current1=list1
        current2=list2
        temp=result=ListNode()
        while current1 is not None and current2 is not None:
            if current1.val<=current2.val:
                temp.next=ListNode(current1.val)
                current1=current1.next
            else:
                temp.next=ListNode(current2.val)
                current2=current2.next
            temp=temp.next
        if current1 is not None:
            temp.next=current1
        if current2 is not None:
            temp.next=current2
        return result.next