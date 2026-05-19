class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s,t=nums1[0],nums1[-1]
        nums1=set(nums1)
        nums2=set(nums2)
        for num in range(s,t+1):
            if num in nums1 and num in nums2:
                return num
        return -1