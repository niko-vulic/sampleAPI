# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.



class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "lengthOfLongestSubstring"

    def defineTestCases(self):
        self.testCases.append("abcabc")
        self.testCases.append("bbbeeee")
        self.testCases.append("12341234512345612345")

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + case + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def lengthOfLongestSubstring(self, s: str) -> int:
        # Moving sub-array problem. We use a second array to store the current, and a maxLength counter which is
        # recalculated when the current is increased. No further variables are required
        maxLength = 0

        # Its possible a dict would be faster runtime than an array
        currentSubstring  = []


        for i in s:
            if i not in currentSubstring:
                # If the element doesn't already exist, add it and recalc max length
                currentSubstring.append(i)

                # Everytime we increase the currentSubstring, it might be possible to become a new max
                if len(currentSubstring) > maxLength:
                    maxLength = len(currentSubstring)
            else:
                # If the element exists, slice the current array from the element and append the same char to the end
                indexOfElement = currentSubstring.index(i)
                currentSubstring = currentSubstring[indexOfElement+1:]
                currentSubstring.append(i)

        return maxLength

if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()