class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        rec=0
        cnt=0
        n=len(s)
        for i in range(n-1,-1,-1):
            if s[i]=='1':
                if rec+(1<<cnt)<=k:
                    rec+=(1<<cnt)
                    cnt+=1
            else:
                cnt+=1
        return cnt
                    
