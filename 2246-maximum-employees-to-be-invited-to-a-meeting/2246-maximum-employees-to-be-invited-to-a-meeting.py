class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        deg = [0] * n
        for f in favorite:
            deg[f] += 1 

        rg = [[] for _ in range(n)] 
        q = deque(i for i, d in enumerate(deg) if d == 0)
        while q: 
            x = q.popleft()
            y = favorite[x] 
            rg[y].append(x)
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)


        def rdfs(x: int) -> int:
            max_depth = 1
            for son in rg[x]:
                max_depth = max(max_depth, rdfs(son) + 1)
            return max_depth

        max_ring_size = sum_chain_size = 0
        for i, d in enumerate(deg):
            if d == 0: continue

      
            deg[i] = 0  
            ring_size = 1  
            x = favorite[i]
            while x != i:
                deg[x] = 0  
                ring_size += 1
                x = favorite[x]

            if ring_size == 2:  
                sum_chain_size += rdfs(i) + rdfs(favorite[i])  
            else:
                max_ring_size = max(max_ring_size, ring_size)  
        return max(max_ring_size, sum_chain_size)
