# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

from typing import List

class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "groupAnagrams"

    def defineTestCases(self):
        self.testCases.append(["eat","tea","tan","ate","nat","bat"])
        #self.testCases.append(["a"])
        self.testCases.append(["","b",""])
        #self.testCases

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultDict = {}

        for item in strs:
            key = ''.join(sorted(item))
            if key in resultDict:
                resultDict[key].append(item)
            else:
                resultDict[key] = [item]

        return list(resultDict.values())

    def groupAnagrams_working_for_short_arrays(self, strs: List[str]) -> List[List[str]]:
        resultSet = []

        while strs:
            candidate = strs.pop()
            subset = []
            isValidMatch = [True] * len(strs)

            for other in range(len(strs)):
                if len(candidate) != len(strs[other]):
                    isValidMatch[other] = False
                else:
                    for str_char in candidate:
                        if isValidMatch[other] != False:
                        #print("Comparing -" + candidate + "- and -" + strs[other])
                            if candidate.count(str_char) != strs[other].count(str_char):
                                isValidMatch[other] = False

            for match in range(len(strs)):
                if isValidMatch[match]:
                    subset.append(strs[match])

            print("Candidate is: " + candidate + " ,matches found:" + str(subset))
            for item in subset:
                print("Attempting to remove:" + item)
                strs.remove(item)

            # Append the candidate before returning, else it will fail on remove as we already popped it
            subset.append(candidate)
            resultSet.append(subset)
        return resultSet

if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()