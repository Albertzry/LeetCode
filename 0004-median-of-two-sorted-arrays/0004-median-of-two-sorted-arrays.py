class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3=nums1+nums2
        nums3.sort()
        n=len(nums3)
        if n%2==0:
            r=nums3[n//2-1]+nums3[n//2]
            re=r/2.0
        else :
            re=nums3[n//2]
        return re