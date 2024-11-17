class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = inf
        s = list(accumulate(nums, initial=0))  
        q = deque()
        for i, cur_s in enumerate(s):
            while q and cur_s - s[q[0]] >= k:
                ans = min(ans, i - q.popleft())  
            while q and s[q[-1]] >= cur_s:
                q.pop() 
            q.append(i)
        return ans if ans < inf else -1