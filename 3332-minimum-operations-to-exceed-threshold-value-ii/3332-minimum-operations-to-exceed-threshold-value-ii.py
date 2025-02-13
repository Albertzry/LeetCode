class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        h = nums[:]
        heapify(h)
        while h[0] < k:
            x = heappop(h)
            y = heappop(h)
            heappush(h, x + x + y)
            res += 1
        return res
