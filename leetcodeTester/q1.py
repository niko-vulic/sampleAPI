# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
from typing import List


class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "twoSum"

    def defineTestCases(self):
        self.testCases.append([[2,3,4], 6])
        self.testCases.append([[1,4,7,8],9])
        #self.testCases.append("12341234512345612345")

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case[0], case[1])))

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for index, element in enumerate(nums):
            elementToFind = target-element
            if elementToFind in hashMap:
                #print("Found " + str(elementToFind))
                return [hashMap[elementToFind] ,index]
            else:
                #print("Not found, adding element:" + str(element))
                hashMap[element] = index


        result = []
        return result

if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()