class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit
        profit = 0
        
        # low value index
        left = 0
        
        #high value index
        right = 1

        for i in range(len(prices)):
            if prices[i] <= prices[left]:
                left = i
                right = i
            
            if prices[i] - prices[left] >= profit:
                profit = prices[i] - prices[left]

            right += 1


        return profit