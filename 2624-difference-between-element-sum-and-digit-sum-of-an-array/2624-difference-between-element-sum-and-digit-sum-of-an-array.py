class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num1=sum(nums)
        num2=0
        for num in nums:
            while num:
                num2+=(num%10)
                num//=10
        return num1-num2