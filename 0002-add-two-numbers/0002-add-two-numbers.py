# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re=0
        result=current=ListNode(0)

        while l1 or l2 :
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            sum =x+y+re
            current.next=ListNode(sum%10)
            current=current.next
            re=sum//10

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if re:
            current.next=ListNode(re)
        return result.next