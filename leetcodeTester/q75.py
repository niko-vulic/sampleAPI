# 75. Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
# are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

from typing import List

class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "sortColors"

    def defineTestCases(self):
        #self.testCases.append([0, 1, 2])
        #self.testCases.append([0, 2, 2, 0, 1, 2, 2, 2])
        self.testCases.append([2, 0, 2, 1, 1, 0])


    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def sortColors(self, nums: List[int]) -> None:
        # One pass algorithm - get the leftmost 0
        zero_counter = 0
        while zero_counter < len(nums) and nums[zero_counter] == 0:
            zero_counter += 1

        # Get the rightmost 2 - this is the index we move any new 2s to
        twos_counter = len(nums) - 1
        while nums[twos_counter] == 2 and twos_counter >= 0:
            twos_counter -= 1

        # print("Current array:" + str(nums) + " ,zero-index:" + str(zero_counter) + " ,twos-index:" + str(twos_counter))
        for index in range(zero_counter, twos_counter):

            # We make at most len(n) - zero_counter - twos_counter actions. If either limit is reached, we stop
            if index <= twos_counter:
                temp = nums[index]
                if temp == 2:
                    nums[index] = nums[twos_counter]
                    nums[twos_counter] = temp
                    # If we swap a two, move the twos-counter continually left if there are any adjacent
                    while nums[twos_counter] == 2 and twos_counter >= 0:
                        twos_counter -= 1

                temp = nums[index]
                if temp == 0:
                    nums[index] = nums[zero_counter]
                    nums[zero_counter] = temp
                    zero_counter += 1

if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()