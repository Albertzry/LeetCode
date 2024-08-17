# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        before = current = result = ListNode()
        result.next = head
        n = 0
        temp = []
        while current:
            if n == k:
                temp.append(current.val)
                after = current.next
                for i in range(k, 0, -1):
                    before.next = ListNode(temp.pop())
                    before = before.next
                before.next = after
                current = before.next
                n = 0
            elif n < k:
                temp.append(current.val)
                current = current.next
            n += 1
        return result.next