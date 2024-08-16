# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None  or head.next is None:
            return head
        temp=head.next
        head.next=temp.next
        temp.next=head
        head=temp
        current=head
        t=0
        while current is not None and current.next is not None:
            if t%2==1:
                after1=current.next
                if after1.next is None:
                    break
                after2=after1.next
                after1.next=after2.next
                current.next=after2
                after2.next=after1
            current=current.next   
            t+=1
        return head
                