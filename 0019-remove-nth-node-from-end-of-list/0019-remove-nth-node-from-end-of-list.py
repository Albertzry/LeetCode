# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current = head
        num=1
        while current.next!=None:
            current=current.next
            num+=1
        ob = head 
        i=1
        while i<=num:
            if n == num:
                return head.next
            if i == num-n:
                temp = ob.next
                ob.next=temp.next
                break
            else:
                ob = ob.next
                i+=1
        return head
            

