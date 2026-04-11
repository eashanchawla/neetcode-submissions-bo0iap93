class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum, max_profit = prices[0], 0
        cum_profit, current_profit = 0, 0
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1]:
                continue
            elif prices[i] <= prices[i - 1]:
                cum_profit += current_profit
                current_profit = 0
                minimum = prices[i]
            else:
                current_profit = max(current_profit , prices[i] - minimum)

        if current_profit != 0:
            cum_profit += current_profit
        return cum_profit