class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        f = [[1] * n for _ in range(n)]
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    f[j][i] = f[j][i - 1]
                elif s[j] == s[j + 1]:
                    f[j][i] = f[j + 1][i]
                else:
                    f[j][i] = min(f[j][k] + f[k + 1][i] for k in range(j, i))
        return f[0][n - 1]