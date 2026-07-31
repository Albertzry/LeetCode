class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        rc = defaultdict()
        for i,pair in enumerate(cnt.most_common()):
            rc[pair[0]] = i//8 +1
        ans = 0
        for ch in word:
            ans+=rc[ch]
        return ans