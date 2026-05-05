# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        n = 1 
        cur = head
        while cur.next:
            cur = cur.next
            n+=1
        last = cur
        k %= n
        if k == 0:
            return head
        cur = head
        for i in range(n-k-1):
            cur = cur.next
        
        new_head = cur.next
        cur.next = None
        last.next = head
        return new_head
