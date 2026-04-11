class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minimum = float('inf')

        for price in prices:
            if price <= minimum:
                # create new minimum
                minimum = price
            else:
                profit = price - minimum
                max_profit = max(max_profit, profit)
        return max_profit