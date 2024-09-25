class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import defaultdict
        trie = lambda: defaultdict(trie)
        root = trie()
        for word in words:
            cur = root
            for c in word:
                cur = cur[c]
                cur[None] = cur.get(None, 0) + 1
        ans = []
        for word in words:
            cur, sum = root, 0
            for c in word:
                cur = cur[c]
                sum += cur[None]
            ans.append(sum)
        return ans
            