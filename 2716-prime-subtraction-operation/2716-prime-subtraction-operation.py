class Solution(object):
    def primeSubOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import math
        def judge_prime(number):
            for i in range(2, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    return False
            return True
        n=len(nums)
        if n==1:
            return True
        for i, num in enumerate(nums):
            if i==n-1 and num>nums[i-1]:
                return True
            if i == 0:
                for temp in range(num - 1, 1, -1):
                    if judge_prime(temp):
                        nums[i] -= temp
                        break
            else:
                for temp in range(num - 1, 1, -1):
                    if judge_prime(temp) and num-temp>nums[i-1]:
                        nums[i] -= temp
                        break
            if i<n-1 and nums[i]>=nums[i+1]:
                    return False
