# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        left = 0
        right = 1

        if len(prices) <= 1:
            return 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right

            max_profit = max(max_profit, profit)

            right += 1

        return max_profit
            
