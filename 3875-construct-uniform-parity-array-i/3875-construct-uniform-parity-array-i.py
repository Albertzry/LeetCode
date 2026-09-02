class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True
        n = len(nums1)
        o,e = 0,0
        for num in nums1:
            if num%2 ==0:
                e+=1
            else:
                o+=1
        
        
