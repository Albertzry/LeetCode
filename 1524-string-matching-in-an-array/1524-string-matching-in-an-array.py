class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        for i, x in enumerate(words):
            for j, y in enumerate(words):
                if j != i and x in y:
                    ans.append(x)
                    break
        return ans
