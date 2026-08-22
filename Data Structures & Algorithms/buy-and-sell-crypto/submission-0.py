class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
    
        size = len(prices)
        left, right = 0, 1
        maxProfit = 0

        while right < size:

            profit = prices[right] - prices[left]
            
            if profit > maxProfit:
                maxProfit = profit

            if prices[right] < prices[left]:
                left = right
                
            right+=1

        return maxProfit

        
            

            