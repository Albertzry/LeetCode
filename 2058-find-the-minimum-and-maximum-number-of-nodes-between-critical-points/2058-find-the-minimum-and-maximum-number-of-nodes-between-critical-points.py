# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next

        n = len(nums)
        
        pos = []
        ans = [-1,-1]
        for i in range(0,n-2):
            if nums[i+1] > nums[i] and nums[i+1]>nums[i+2]:
                pos.append(i+1)
            elif nums[i+1] < nums[i] and nums[i+1]<nums[i+2]:
                pos.append(i+1)
            if len(pos)>=2:
                ans[0] =min(ans[0],pos[-1]-pos[-2]) if ans[0]!=-1 else pos[-1]-pos[-2]
        if len(pos) >=2:
            ans[1] = pos[-1]-pos[0]

        return ans
           
        