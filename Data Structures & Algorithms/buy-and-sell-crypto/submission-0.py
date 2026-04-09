class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Initialize the minimum price to a very large value
        # and the max profit to 0
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update min_price if the current price is lower
            if price < min_price:
                min_price = price
            
            # Calculate potential profit if we sold today
            current_profit = price - min_price
            
            # Update max_profit if current_profit is the best we've seen
            if current_profit > max_profit:
                max_profit = current_profit
                
        return max_profit
        