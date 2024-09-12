class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        allowed = set(allowed)
        for i in range(len(words)):
            temp = set(words[i])
            if allowed|temp == allowed:
                res+=1
        return res