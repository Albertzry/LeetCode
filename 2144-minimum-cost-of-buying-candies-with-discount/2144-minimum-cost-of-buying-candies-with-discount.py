class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        ans = 0 
        n = len(cost)
        l = 0
        while l<n:
            ans += cost[l]
            if l < n-2:
                ans += cost[l+1]
                l+=3
                continue
            elif l == n-2:
                ans += cost[l+1]
                break
            else:
                break
        return ans
        
