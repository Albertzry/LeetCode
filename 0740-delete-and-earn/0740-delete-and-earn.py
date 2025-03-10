class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        temp=[]
        nums.sort()
        map=dict()
        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]]+=1
            else:
                map[nums[i]]=1
                temp.append(nums[i])
        n=len(temp)
        dp=[0]*(n+1)
        dp[1]=map[temp[0]]*temp[0]
        for i in range(2,n+1):
            if temp[i-1]==temp[i-2]+1:
                dp[i]=max(dp[i-2]+map[temp[i-1]]*temp[i-1],dp[i-1])
            else:
                dp[i]=dp[i-1]+map[temp[i-1]]*temp[i-1]
        return dp[-1] 