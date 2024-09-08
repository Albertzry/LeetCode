# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        n=0
        current = head
        while current is not None:
            n+=1
            current=current.next
        result = []
        current = head
        if n <= k:
            for i in range(k):
                if i < n:
                    result.append(current)
                    temp = current.next
                    current.next = None
                    current = temp
                else:
                    result.append(None)
        else:
            remainder = n % k
            cnt = n // k
            t=0
            for i in range(n):
                if remainder == 0 and cnt==1:
                    while current is not None:
                        result.append(current)
                        temp = current.next
                        current.next = None
                        current = temp
                    break
                t+=1
                if t == 1:
                    result.append(current)
                    current=current.next
                elif remainder > 0 and t == cnt+1:
                    remainder-=1
                    temp=current.next
                    current.next=None
                    current=temp
                    t=0
                elif remainder == 0 and t == cnt:
                    temp=current.next
                    current.next=None
                    current=temp
                    t=0
                else:
                    current = current.next
        return result
