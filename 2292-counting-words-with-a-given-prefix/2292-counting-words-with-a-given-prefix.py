class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        ans = 0
        for word in words:
            if word.startswith(pref):
                ans+=1
        return ans