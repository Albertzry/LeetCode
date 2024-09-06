class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find_factors(n):
            res=set()
            from math import sqrt
            for i in range(1,int(sqrt(n))+1):
                if n%i==0:
                    res.add(i)
                    res.add(n//i)
            return list(res)
        result=0
        for i in range(len(nums)):
            temp= find_factors(nums[i])
            if len(temp) == 4:
                result += sum(temp)
        return result