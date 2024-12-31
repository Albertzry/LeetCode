class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        days = set(days)
        @cache  
        def dfs(i: int) -> int:
            if i <= 0:
                return 0
            if i not in days:
                return dfs(i - 1)
            return min(dfs(i - 1) + costs[0], dfs(i - 7) + costs[1], dfs(i - 30) + costs[2])
        return dfs(last_day)
