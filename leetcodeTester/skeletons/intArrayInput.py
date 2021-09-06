# ##. Int Array

from typing import List

class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "tempFuncName"

    def defineTestCases(self):
        self.testCases.append([0, 1, 2])

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def tempFuncName(self, nums: List[int]) -> int:
        print(nums)
        return 0

if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()