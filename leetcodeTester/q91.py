# 91. Decode Ways
# A message containing letters from A-Z can be encoded into numbers using the following mapping:
#
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
#
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the
# mapping above (there may be multiple ways). For example, "11106" can be mapped into:
#
#     "AAJF" with the grouping (1 1 10 6)
#     "KJF" with the grouping (11 10 6)
#
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
# Given a string s containing only digits, return the number of ways to decode it.
# The answer is guaranteed to fit in a 32-bit integer.

class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "numDecodings"

    def defineTestCases(self):
        #self.testCases.append("102938126012059328905623012010210")
        #self.testCases.append("2232")
        #self.testCases.append("12")
        self.testCases.append("226")
        self.testCases.append("123123")
        self.testCases.append("111111111111111111111111111111111111111111111")

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case)))


    # Have to abandon this approach, takes too long, fails test case: 111111111111111111111111111111111111111111111
    # Note this does give the right result but it needs to be optimized
    def numDecodings(self, s: str) -> int:

        # Map 10 and 20 to unique chars - any extra 0s are an invalid string
        s = s.replace('10', 'a').replace('20', 'b')
        if '0' in s:
            #print("invalid test case")
            return 0

        finalCount = self.getValidCount(s)
        #print("Number of valid possibilities: " + str(finalCount))
        return finalCount[s]

    # Have to abandon this approach, takes too long, fails test case: 111111111111111111111111111111111111111111111
    def getValidCount(self, s: str):
        # Define stopping cases - if single digit or a/b, then end-case reached
        if len(s) == 1:
            return {s: 1}
        # If s contains a '10' or '20', only 1 possible combo
        elif len(s) == 2 and ('a' in s or 'b' in s):
            return {s: 1}
        # Else if s can be split into 2 nums, 2 possible combos [26]=>2,6 + 26, else just one possibility
        elif len(s) == 2:
            if int(s) <= 26:
                return {s: 2}
            else:
                return {s: 1}

        # Otherwise we recursively split the string further if it doesnt contain a or b, else only 1 way to split it
        if s[0] == 'a' or s[0] == 'b':
            finalCount = self.getValidCount(s[1:])
            finalCount[s] = finalCount[s[1:]]
        elif s[1] == 'a' or s[1] == 'b':
            finalCount = self.getValidCount(s[2:])
            finalCount[s] = finalCount[s[2:]]
        elif int(s[0:2]) <= 26:
            #print("Path1: Checking substrings:[{s1}] and [{s2}]".format(s1 = s[1:], s2 = s[2:]))
            leftResult = self.getValidCount(s[1:])
            rightResult = {}
            if s[2:] not in leftResult:
                rightResult = self.getValidCount(s[2:])
            finalCount = {**leftResult, **rightResult}
            #
            finalCount[s] = finalCount[s[1:]] + finalCount[s[2:]]
        else:
            #print("Path2: Checking substrings:[{s1}]".format(s1=s[2:]))
            finalCount = self.getValidCount(s[1:])
            finalCount[s] = finalCount[s[1:]]

        countForStringS = 0
        return finalCount

    # Have to abandon this approach, takes too long, fails test case: 111111111111111111111111111111111111111111111
    # Note this does give the right result but it needs to be optimized
    def numDecodings_preOptimized(self, s: str) -> int:

        # Map 10 and 20 to unique chars - any extra 0s are an invalid string
        s = s.replace('10', 'a').replace('20', 'b')
        if '0' in s:
            print("invalid test case")
            return 0

        finalCount = self.getValidCount(s)
        print("Number of valid possibilities: " + str(finalCount))
        return finalCount

    def getValidCount_preOptimized  (self, s: str):
        # Define stopping cases - if single digit or a/b, then end-case reached
        if len(s) == 1:
            return 1
        # If s contains a '10' or '20', only 1 possible combo
        elif len(s) == 2 and ('a' in s or 'b' in s):
            return 1
        # Else if s can be split into 2 nums, 2 possible combos [26]=>2,6 + 26, else just one possibility
        elif len(s) == 2:
            if int(s) <= 26:
                return 2
            else:
                return 1

        #print("Splitting current string {s}".format(s = s))
        # Otherwise we recursively split the string further if it doesnt contain a or b, else only 1 way to split it
        if s[0] == 'a' or s[0] == 'b':
            finalCount = self.getValidCount(s[1:])
        elif s[1] == 'a' or s[1] == 'b':
            finalCount = self.getValidCount(s[2:])
        elif int(s[0:2]) <= 26:
            #print("Path1: Checking substrings:[{s1}] and [{s2}]".format(s1 = s[1:], s2 = s[2:]))
            left = self.getValidCount(s[1:])
            right = self.getValidCount(s[2:])
            finalCount = left + right
        else:
            #print("Path2: Checking substrings:[{s1}]".format(s1=s[2:]))
            finalCount = self.getValidCount(s[1:])
        return finalCount


if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()