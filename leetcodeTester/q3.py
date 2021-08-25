# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.



class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "lengthOfLongestSubstring"

    def defineTestCases(self):
        self.testCases.append("abcabc")
        self.testCases.append("bbbeeee")

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + case + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def lengthOfLongestSubstring(self, s: str) -> int:
        totalLength = len(s)
        current  = []

        for i in s:
            pass

        maxLength = 0

        return maxLength

if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()