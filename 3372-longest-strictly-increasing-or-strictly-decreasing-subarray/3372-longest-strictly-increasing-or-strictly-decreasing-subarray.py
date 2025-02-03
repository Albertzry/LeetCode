class Solution:
    def longestMonotonicSubarray(self, a: List[int]) -> int:
        ans = 1
        i, n = 0, len(a)
        while i < n - 1:
            if a[i + 1] == a[i]:
                i += 1  
                continue
            i0 = i  
            inc = a[i + 1] > a[i]  
            i += 2  
            while i < n and a[i] != a[i - 1] and (a[i] > a[i - 1]) == inc:
                i += 1
            ans = max(ans, i - i0)
            i -= 1
        return ans
