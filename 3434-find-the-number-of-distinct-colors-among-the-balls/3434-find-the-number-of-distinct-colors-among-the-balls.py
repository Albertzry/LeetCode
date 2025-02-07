class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = []
        color = {}
        cnt = defaultdict(int)
        for x, y in queries:
            if x in color:
                c = color[x]
                cnt[c] -= 1
                if cnt[c] == 0:
                    del cnt[c]
            color[x] = y
            cnt[y] += 1
            ans.append(len(cnt))
        return ans
