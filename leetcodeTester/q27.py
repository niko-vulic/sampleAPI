# 27. Remove Element
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.
#
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed
# in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the
# first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

from typing import List

class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "removeElement"

    def defineTestCases(self):
        self.testCases.append([[2, 3, 4], 3])
        self.testCases.append([[1, 4, 7, 8], 5])
        self.testCases.append([[-1, 0, 4, 7], 4])
        self.testCases.append([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 12])
        self.testCases.append(([[0, 1, 2, 2, 3, 0, 4, 2], 2]))
        self.testCases.append([[3, 3], 3])
        self.testCases.append([[3, 3, 3, 3], 3])
        self.testCases.append([[2], 3])
        self.testCases.append([[3, 2, 2, 3], 3])

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case[0], case[1])))

    def removeElement(self, nums: List[int], val: int) -> int:

        popCounter = 0
        for index in range(len(nums)):
            # print("current item:" + str(index) + "and popCounter:" + str(popCounter) + "  in array:" + str(nums))
            if nums[index - popCounter] == val:
                nums.pop(index - popCounter)
                popCounter += 1

        return len(nums)





    def removeElement2(self, nums: List[int], val: int) -> int:

        nextArrayIndexToReplace = len(nums) -1
        valsFound = 0

        for index in range(len(nums)):
            if nums[index] == val:
                valsFound += 1


                while nextArrayIndexToReplace > 0 and nums[nextArrayIndexToReplace] == val:
                    nextArrayIndexToReplace -= 1
                print("Next element to replace:" + str(nextArrayIndexToReplace))

                # while nums[index] == val and index < nextArrayIndexToReplace and nextArrayIndexToReplace >= 0:
                temp = nums[index]
                nums[index] = nums[nextArrayIndexToReplace]
                nums[nextArrayIndexToReplace] = temp
                print("valsFound: " + str(valsFound) + ",current Array:" + str(nums))

        print(nums[:-valsFound])
        return len(nums) - valsFound





if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()