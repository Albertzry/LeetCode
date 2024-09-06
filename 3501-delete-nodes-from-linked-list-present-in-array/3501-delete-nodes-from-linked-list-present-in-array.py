# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums = set(nums)
        start = before = ListNode()
        start.next = current = head
        while current is not None:
            if current.val in nums:
                before.next=current.next
            else:before=before.next
            current=current.next
        return start.next