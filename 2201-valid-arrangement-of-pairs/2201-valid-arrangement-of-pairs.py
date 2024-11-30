class Solution(object):
    def validArrangement(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: List[List[int]]
        """
        edges = defaultdict(list)
      
        indeg, outdeg = Counter(), Counter()
        for x, y in pairs:
            edges[x].append(y)
            indeg[y] += 1
            outdeg[x] += 1
        
        
        start = pairs[0][0]
        for x in outdeg:
           
            if outdeg[x] == indeg[x] + 1:
                start = x
                break
        
        ans = list()
        
        def dfs(u):
            while edges[u]:
                v = edges[u].pop()
                dfs(v)
                ans.append([u, v])
        
        dfs(start)
        return ans[::-1]

