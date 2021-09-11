# 97. Interleaving String
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
#
# An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:
#
#     s = s1 + s2 + ... + sn
#     t = t1 + t2 + ... + tm
#     |n - m| <= 1
#     The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
#
# Note: a + b is the concatenation of strings a and b.

class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "isInterleave"

    def defineTestCases(self):
        #self.testCases.append(["aabcc", "dbbca", "aadbbcbcac"])
        #self.testCases.append(["aabcc", "dbbca", "aadbbbaccc"])
        self.testCases.append(["abc", "abde", "abcabcde"])

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case[0], case[1], case[2])))

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        dp = [[False for i in range(len(s1)+1)] for j in range(len(s2)+1)]

        # Sample array: abc, abd, ababdc
        # For pos 3 - either 112 or 221 - for paths from array1 or array2
        for i
        print(dp)

if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()
