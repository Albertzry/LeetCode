class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        m = len(words[0]);n = len(target)
        cnt = [Counter() for _ in range(m)]
        for word in words:
            for i in range(m):
                cnt[i][word[i]] += 1
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            f[i][0] = 1
        for i in range(m):
            for j in range(n):
                f[i + 1][j + 1] = (f[i][j + 1] + cnt[i][target[j]] * f[i][j]) % MOD
        return f[-1][-1]
