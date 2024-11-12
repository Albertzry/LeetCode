class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        items.sort()
        i,n=0,len(items)
        while i<n:
            if i > 0:
                if items[i][0] == items[i - 1][0]:
                    items[i - 1][1] = max(items[i][1], items[i - 1][1])
                    items.remove(items[i])
                    n-=1
                    continue
                items[i][1] = max(items[i][1], items[i - 1][1])
            i+=1
        ans = []
        n = len(items)
        for query in queries:
            if query < items[0][0]:
                ans.append(0)
                continue
            l, r = 0, n - 1
            m = int((l + r) / 2)
            while True:
                if items[m][0] == query:
                    break
                elif items[m][0] < query:
                    if m < n - 1 and items[m + 1][0] > query or m == n - 1:
                        break
                    l = m
                    m = int((l + r) / 2) + 1
                else:
                    r = m
                    m = m = int((l + r) / 2)
            ans.append(items[m][1])
        return ans