# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        current = result = ListNode()
        q=[]
        n=0
        for i in range(len(lists)):
            temp=lists[i]
            while temp is not None:
                heapq.heappush(q,temp.val)
                temp=temp.next
                n+=1
        for i in range(n):
            current.next=ListNode(heapq.heappop(q))
            current=current.next
        return result.next

