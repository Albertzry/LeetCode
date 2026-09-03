class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        mn = min(nums1)
        flag = False
        for num in nums1:
            if num %2 ==1:
                flag = True
                break
        if mn%2 == 0 and flag == True:
            return False
        return True
                