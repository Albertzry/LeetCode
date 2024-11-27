class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        def bfs(node_list, cnt):
            temp = set()
            cnt += 1
            for node in node_list:
                for next_node in connects[node]:
                    if next_node == n - 1:
                        return cnt
                    temp.add(next_node)
            return bfs(temp, cnt)

        connects = defaultdict(list)
        for i in range(n - 1):
            connects[i].append(i + 1)

        ans = []
        for query in queries:
            connects[query[0]].append(query[1])
            ans.append(bfs({0},0))
        return ans