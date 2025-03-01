class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack=[]
        for i in range(n):
            if nums[i]!=0:
                if i<n-1 and nums[i]==nums[i+1]:
                    nums[i]*=2
                    nums[i+1]=0
                stack.append(nums[i])
        m=len(stack)
        stack+=[0]*(n-m)
        return stack
                