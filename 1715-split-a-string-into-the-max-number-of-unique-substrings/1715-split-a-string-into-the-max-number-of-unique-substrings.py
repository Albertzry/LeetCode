class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        def backtrack(ans, p):
            if p == n:
                res[0] = max(res[0], len(ans))
                return
            for i in range(p + 1, n+1):
                if s[p:i] in ans:
                    continue
                else:
                    ans.add(s[p:i])
                    backtrack(ans, i)
                    ans.remove(s[p:i])

        ans = set()
        res = [0]
        backtrack(ans, 0)
        return res[0]