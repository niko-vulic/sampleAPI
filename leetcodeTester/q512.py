# 152. Maximum Product Subarray 

# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
# It is guaranteed that the answer will fit in a 32-bit integer.
# A subarray is a contiguous subsequence of the array.

from typing import List
import math

class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "maxProduct"

    def defineTestCases(self):
        self.testCases.append([0, 1, 2])
        self.testCases.append([6, -4, -2, -1, 0, 25, 0, -5, 0, -8])

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def maxProduct(self, nums: List[int]) -> int:



        localMax = nums[0]
        localMin = nums[0]
        globalMax = nums[0]
        globalMin = nums[0]

        for i in range(1, len(nums)):

            if nums[i] == 0:
                localMax = 0
                localMin = 0
            elif localMax == 0:
                localMax = nums[i]
                localMin = nums[i]
            else:
                # Store as tempMin, tempMax, else it will be re-calculated in between line 45 and line 46 multiple times
                tempMin = localMin * nums[i]
                tempMax = localMax * nums[i]

                localMin = min(nums[i], tempMin, tempMax)
                localMax = max(nums[i], tempMin, tempMax)


            if localMax > globalMax:
                globalMax = localMax
            if localMin < globalMin:
                globalMin = localMin

        print("globalMax:" + str(globalMax) + " , globalMin:" + str(globalMin))
        return globalMax


    # Fully working in leetcode, pre-optimization
    def maxProduct2(self, nums: List[int]) -> int:

        # Maintain a tuple structure
        # [maxValue, maxPos, minValue, minPos]
    
        localMax = [-math.inf] * len(nums)
        localMin = [math.inf] * len(nums)

        localMax[0] = nums[0]
        localMin[0] = nums[0]
        globalMax = nums[0]
        globalMin = nums[0]

        for i in range(1, len(nums)):

            if nums[i] == 0:
                localMax[i] = 0
                localMin[i] = 0
            elif localMax[i-1] == 0:
                localMax[i] = nums[i]
                localMin[i] = nums[i]
            else:
                localMin[i] = min(nums[i], localMin[i-1] * nums[i], localMax[i-1] * nums[i])
                localMax[i] = max(nums[i], localMax[i-1] * nums[i], localMin[i-1] * nums[i])

                #if nums[i] > 0:
                #    localMax[i] = localMax[i-1] * nums[i]
                #    localMin[i] = localMin[i-1] * nums[i]
                #else:
                #    localMin[i] = localMax[i-1] * nums[i]
                #    localMax[i] = localMin[i-1] * nums[i]

            if localMax[i] > globalMax:
                globalMax = localMax[i]
            if localMin[i] < globalMin:
                globalMin = localMin[i]

        print("globalMax:" + str(globalMax) + " , globalMin:" + str(globalMin))
        return globalMax
        
        
        
    def kadane(nums):
        localMax = [-math.inf] * len(nums)
        localMax[0] = nums[0]
        globalMax = nums[0]

        for i in range(1, len(nums)):
            localMax[i] = max(nums[i], nums[i] + localMax[i - 1])

            if localMax[i] > globalMax:
                globalMax = localMax[i]

        return globalMax

if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()