class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = left = 0
        cnt = [0] * 3
        for c in s:
            cnt[ord(c) - ord('a')] += 1
            while cnt[0] and cnt[1] and cnt[2]:
                cnt[ord(s[left]) - ord('a')] -= 1
                left += 1
            ans += left
        return ans
