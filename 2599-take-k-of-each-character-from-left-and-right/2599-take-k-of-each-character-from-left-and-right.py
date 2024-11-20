class Solution(object):
    def takeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import Counter
        cnt = Counter(s)  
        if any(cnt[c] < k for c in "abc"):
            return -1

        mx = left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1  
            while cnt[c] < k:  
                cnt[s[left]] += 1  
                left += 1
            mx = max(mx, right - left + 1)
        return len(s) - mx
