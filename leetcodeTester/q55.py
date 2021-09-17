# ##. Int Array

from typing import List

class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "canJump"

    def defineTestCases(self):
        self.testCases.append([0, 1, 2])
        self.testCases.append([2,3,1,1,4])

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def canJumpLambda(self, nums: List[int]) -> bool:

        return reduce(lambda x: )

        if len(nums) == 1: return True
        currentJumpCounter = nums[0]

        for i in range(len(nums)):
            currentJumpCounter = currentJumpCounter - 1
            if currentJumpCounter >= 0:
                currentJumpCounter = max(currentJumpCounter, nums[i])
            else:
                return False

        return True

    def canJump(self, nums: List[int]) -> bool:


        if len(nums) == 1: return True
        currentJumpCounter = nums[0]

        for i in range(len(nums)):
            currentJumpCounter = currentJumpCounter - 1
            if currentJumpCounter >= 0:
                currentJumpCounter = max(currentJumpCounter, nums[i])
            else:
                return False

        return True

    def canJumpPreoptimized(self, nums: List[int]) -> bool:

        if len(nums) == 1: return True

        dp = [-1] * len(nums)
        dp[0] = nums[0]
        currentJumpCounter = dp[0]

        for i in range(len(nums)):
            currentJumpCounter = currentJumpCounter - 1
            if currentJumpCounter >= 0:
                currentJumpCounter = max(currentJumpCounter, nums[i])
                dp[i] = currentJumpCounter
            else:
                return False

        return dp[-1] > -1

if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()