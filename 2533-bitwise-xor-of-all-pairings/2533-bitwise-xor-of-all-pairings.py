class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums2) % 2: ans ^= reduce(xor, nums1)
        if len(nums1) % 2: ans ^= reduce(xor, nums2)
        return ans
