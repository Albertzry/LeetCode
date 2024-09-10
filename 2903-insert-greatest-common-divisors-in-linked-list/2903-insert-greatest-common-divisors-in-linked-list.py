# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def find_divisors(a,b):
            while b != 0:
                a, b = b, a % b
            return a
        start = before =  ListNode()
        start.next=current=head
        while current:
            if before.val == 0:
                current=current.next
                before=before.next
            else:
                temp=find_divisors(before.val,current.val)
                before.next=ListNode(temp)
                before.next.next=current
                before=current
                current=current.next
        return start.next