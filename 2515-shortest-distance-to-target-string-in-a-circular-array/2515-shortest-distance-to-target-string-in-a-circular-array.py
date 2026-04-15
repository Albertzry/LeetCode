class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        words*=3
        start = n+startIndex
        ans = 2*n
        for i,word in enumerate(words):
            if word == target:
                ans = min(ans,abs(start-i))
        return ans if ans!=2*n else -1
