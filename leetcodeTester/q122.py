# 121. Best Time to Buy and Sell Stock II

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time
# However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

from typing import List

class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "maxProfit"

    def defineTestCases(self):
        #self.testCases.append([0, 1, 2])
        self.testCases.append([4, 1, 3, 5, 2, 7])
        self.testCases.append([3, 2, 1])
        self.testCases.append([7, 1, 5, 3, 6, 4])

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def maxProfit(self, prices: List[int]) -> int:

        # We track the peaks and valleys and sum them in a greedy approach
        valley = prices[0]
        peak = prices[0]
        sum = 0

        for i in range(1, len(prices)):
            # 2 possibilities, continuing into a valley from existing decrease, or from a peak into new valley
            if prices[i] < prices[i-1]:
                # If previous value is peak, sum the existing before resetting
                if prices[i-1] == peak:
                    sum += (peak - valley)
                    peak = 0
                # Strictly decreasing or net new, any case of i < i-1 is the newest valley
                valley = prices[i]
            elif prices[i] > prices[i-1]:
                # Any increase in height is a new peak, either continuing a climb i-2<i-1<i or right after valley
                peak = prices[i]

        # We add any remaining peak-valley leftover at the end if one is found
        if peak > 0:
            sum += peak - valley

        return sum

if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()