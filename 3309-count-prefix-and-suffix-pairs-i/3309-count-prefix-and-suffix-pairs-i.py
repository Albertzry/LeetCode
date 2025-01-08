class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def isPrefixAndSuffix(s1,s2):
            return s2.startswith(s1) and s2.endswith(s1)
        n=len(words)
        ans=0
        for i in range(n-1):
            for j in range(i+1,n):
                ans+=isPrefixAndSuffix(words[i], words[j])
        return ans