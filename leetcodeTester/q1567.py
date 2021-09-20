# 1567. Maximum Length of Subarray With Positive Product

# Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.
# A subarray of an array is a consecutive sequence of zero or more values taken out of that array.
# Return the maximum length of a subarray with positive product.

from typing import List

class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "getMaxLen"

    def defineTestCases(self):
        #self.testCases.append([0, 1, 2])
        self.testCases.append([6, -4, -2, -1, 0, 25, 0, -5, 0, -8])
        self.testCases.append([6, -4, 1, 1, 1, -4, -5, 0, 1])
        self.testCases.append([-1, 2, 2, 3])

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def getMaxLen(self, nums: List[int]) -> int:
        
        # Same approach as problem Q152 except we calculate max(length) instead of max(value)
        
        leftmostNegative = 0 if nums[0] < 0 else -1
        countNeg = 1 if nums[0] < 0 else 0
        rightmostNegative = 0 if nums[0] < 0 else -1
        #
        lenCurr = 1 if nums[0] != 0 else 0
        globalMax = 1 if nums[0] > 0 else 0

        for i in range(1, len(nums)):

            # If current value is 0, reset
            if nums[i] == 0:
                lenCurr = 0
                leftmostNegative = -1
                rightmostNegative = -1
                countNeg = 0
            # Else if value is net new, init to 1
            elif lenCurr == 0:
                lenCurr = 1
            # Increase the current length
            else:
                lenCurr += 1

            # If first element is neg, set it to leftMax
            if nums[i] < 0 and leftmostNegative == -1:
                leftmostNegative = i
                rightmostNegative = i
                countNeg += 1
            elif nums[i] < 0:
                rightmostNegative = i
                countNeg += 1

            # For the purposes of calculating max, we should calculate only pos values
            if countNeg % 2 == 0:
                if lenCurr > globalMax:
                    globalMax = lenCurr
            # Case negative num, calc the lengths of leftmost + rightmost negative lengths
            # Only calc when countNeg > 2 to avoid cases of same left/right
            elif countNeg > 2:
                leftMax = i - leftmostNegative
                rightMax = lenCurr - (i - rightmostNegative + 1)

                if max(leftMax, rightMax) > globalMax:
                    globalMax = max(leftMax, rightMax)
            else:
                leftMax = i - leftmostNegative
                if leftMax > globalMax:
                    globalMax = leftMax

            s = 2

        print("globalMax:" + str(globalMax))
        return globalMax

if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()