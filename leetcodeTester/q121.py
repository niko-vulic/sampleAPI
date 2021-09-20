# 121. Best Time to Buy and Sell Stock 

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List

class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "maxProfit"

    def defineTestCases(self):
        self.testCases.append([0, 1, 2])
        self.testCases.append([4, 1, 3, 5, 2, 7])
        self.testCases.append([3, 2, 1])

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def maxProfit(self, prices: List[int]) -> int:
        
        minBuy = [0] * len(prices)
        minBuy[0] = prices[0]
        maxDiff = 0
        
        for i in range(1, len(prices)):
            minBuy[i] = min(prices[i], minBuy[i-1])

            currDiff = prices[i] - minBuy[i]
            if currDiff > maxDiff: maxDiff = currDiff

        return maxDiff

if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()