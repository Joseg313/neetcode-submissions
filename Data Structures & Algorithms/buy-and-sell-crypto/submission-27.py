class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = 1

        for i in range(len(prices)):

            if prices[i] <= prices[left]:
                left = i
                right = i


            if prices[i] >= prices[right] and prices[i] - prices[left] >= profit:
                right = i
                profit = prices[right] - prices[left]

            right += 1

        return profit