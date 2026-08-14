class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        rc = defaultdict(int)
        n = len(s)
        by = set()
        for r in range(n):
            rc[s[r]]+=1
            if rc[s[r]] >2:
                by.add(s[r])
            while l<=r and by:
                rc[s[l]]-=1
                if rc[s[l]]<=2 and s[l] in by:
                    by.remove(s[l])
                l+=1
            ans = max(ans,r-l+1)
        return ans
                    