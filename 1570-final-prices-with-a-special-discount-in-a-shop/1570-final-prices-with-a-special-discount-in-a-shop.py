class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        ans = [0] * n
        for i, p in enumerate(prices):
            discount = 0
            for j in range(i + 1, n):
                if prices[j] <= p:
                    discount = prices[j]
                    break
            ans[i] = p - discount
        return ans
