'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_low = 10000000000
        max_sell, max_profit = 0, 0
        for p in prices:
            if p < buy_low:
                buy_low = p
            if p > max_sell:
                max_sell = p
            if p - buy_low >= max_profit:
                print(max_sell, buy_low)
                max_profit = p - buy_low
        return max_profit



        
