class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1), len(nums2)
        i,j = 0, 0
        ans = 0
        for i in range(n):
            j = i if j<i else j
            while j< m and  i<=j and nums1[i]<=nums2[j] :
                j+=1
            ans = max(ans, j-i-1)
        
        return ans