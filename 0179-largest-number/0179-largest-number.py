class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums_str = map(str, nums)
        compare = lambda x, y: 1 if x + y < y + x else -1
        nums_str.sort(cmp=compare)
        res = "".join(nums_str)
        if res[0] == "0":
            res = "0"
        return res
            
        
