# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "tempFuncName"

    def defineTestCases(self):
        self.testCases.append("stringHere")
        self.testCases.append("stringHere")
        self.testCases.append("stringHere")

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + case + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def tempFuncName(self, s: str) -> int:
        return 0

if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()