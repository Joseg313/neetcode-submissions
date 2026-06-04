class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #window start and end are indices 
        
        #should hold the lower value index
        window_start = 0
        
        #should hold the higher value index
        window_end = 1
        
        #keeps track of current highest profit for comparison
        profit = 0

        for i in range(len(prices)):
            
            #move window start if we can find a low price than our current low price
            #move window end so that is does not fall behind start
            if prices[i] <= prices[window_start]:
                window_start = i
                window_end = i
            
            # update profit if the next price increases
            if prices[i]-prices[window_start] >= profit:
                profit = prices[window_end]-prices[window_start]
            
            #move window end forward
            window_end += 1
            
        return profit

        
        