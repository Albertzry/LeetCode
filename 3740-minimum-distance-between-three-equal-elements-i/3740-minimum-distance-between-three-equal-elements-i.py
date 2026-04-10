class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        rc = defaultdict(list)
        ans = 3*len(nums)
        for i,num in enumerate(nums):
            rc[num].append(i)
        
        for num in rc:
            n = len(rc[num])
            if n>=3:
                for i in range(0,n-2):
                    ans = min(ans, self.cal_dis(rc[num][i:i+3]))
        
        return ans if ans !=3*len(nums) else -1
                

    def cal_dis(self, pos):
        return abs(pos[0]-pos[1])+abs(pos[2]-pos[1])+abs(pos[0]-pos[2])