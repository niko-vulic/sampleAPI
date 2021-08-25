# 35. Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
from typing import List

class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "searchInsert"

    def defineTestCases(self):
        self.testCases.append([[2, 3, 4], 3])
        self.testCases.append([[1, 4, 7, 8], 5])
        self.testCases.append([[-1, 0, 4, 7], 4])
        self.testCases.append([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 12])

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case[0], case[1])))

    def searchInsert(self, nums: List[int], target: int) -> int:

        # When the last element is reached, return recursively, adding any halfway counters on the return
        if len(nums) == 1:
            if target <= nums[0]:
                return 0
            else:
                return 1

        # fullsize = len(nums)
        halfway = int(len(nums)/2)

        # print("Size of current array" + str(fullsize))
        # print("left half:" + str(nums[:halfway]))
        # print("right half:" + str(nums[halfway:]))

        # As the requirement is O(log n) time, we perform binary search on the array.
        if target < nums[halfway]:
            return self.searchInsert(nums[:halfway], target)
        else:
            return halfway + self.searchInsert(nums[halfway:], target)




if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()