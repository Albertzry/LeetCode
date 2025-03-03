class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        stack1,stack2=[],[]
        cnt=0
        n=len(nums)
        for i in range(n):
            if nums[i]>pivot:
                stack2.append(nums[i])
            elif nums[i]<pivot:
                stack1.append(nums[i])
            else:
                cnt+=1
        return stack1+[pivot]*cnt+stack2