# 121. Best Time to Buy and Sell Stock

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

# method 1
def maxProfit(prices):
    maxAfter = [0]*len(prices)
    mx=0
    ans=0
    for i in range(len(prices)-1, -1, -1):
        mx = max(mx, prices[i])
        maxAfter[i] = mx
    for i in range(len(prices)):
        ans = max(ans, maxAfter[i]-prices[i])
    return ans

# method 2
def maxProfit(prices):
        mx=0
        ans=0
        for i in range(len(prices)-1, -1, -1):
            mx = max(mx, prices[i])
            ans = max(ans, mx-prices[i])
        return ans

# method 3
def maxProfit(prices):
    l, r = 0, 1
    ans = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            ans = max(ans, prices[r] - prices[l])
        else:
            l = r
        r += 1
    return ans