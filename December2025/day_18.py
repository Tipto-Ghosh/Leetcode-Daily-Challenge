from typing import List 

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        
        # profitSum[i] = total profit from day 0 to i-1(exclusive)
        # profitSum[0] = 0
        # profitSum[i + 1] = profitSum[i] + prices[i] * strategy[i]
        profitSum = [0] * (n + 1)
        
        # priceSum[i] = sum of prices from day 0 to day i-1 (exclusive)
        # Used to compute profit after modification where we sell
        priceSum = [0] * (n + 1)
        
        for i in range(n):
            profitSum[i + 1] = profitSum[i] + prices[i] * strategy[i]
            priceSum[i + 1] = priceSum[i] + prices[i]
            
        
        # case-01: No modification in strategy
        res = profitSum[n]
        
        # case-02: Try modifying every possible subarray of length k
        for i in range(k - 1 , n):
            # i = ending index of the window
            # window = [i - k + 1, ..., i]
            
            # Left side profit
            # day [0 to i - k]
            leftProfit = profitSum[i - k + 1]
            
            # Right side profit (unchanged)
            # Days: [i + 1 ... n - 1]
            rightProfit = profitSum[n] - profitSum[i + 1]
            
            # Modified window profit:
            # First k/2 days  -> strategy = 0 (hold)  -> profit = 0
            # Last  k/2 days  -> strategy = 1 (sell)  -> profit = sum of prices
            # Sell part indices:[i - k//2 + 1 ... i]
            changeProfit = priceSum[i + 1] - priceSum[i - k // 2 + 1]
            
            # Total profit after modification
            totalProfit = leftProfit + changeProfit + rightProfit
            
            # take the max of res and current total
            res = max(res , totalProfit)
        
        return res 