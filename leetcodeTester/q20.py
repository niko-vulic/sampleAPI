# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.


class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "isValid"

    def defineTestCases(self):
        self.testCases.append("()")
        self.testCases.append("()[]{}")
        self.testCases.append("(]")

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + case + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def isValid(self, s: str) -> bool:

        openBrackets = '[{('
        mappedBrackets = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []

        for item in s:
            if item in openBrackets:
                stack.append(item)
            else:
                if not stack:
                    return False
                else:
                    if stack.pop() is not mappedBrackets.get(item):
                        return False

        return True if not stack else False

    # Old saved answer from leetcode
    def isValidBackup(self, s: str) -> bool:
        openBrackets = '[{('
        mappedBrackets = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []

        for item in s:
            if item in openBrackets:
                # Any open bracket is tentatively valid so far
                stack.append(item)
            else:
                # Else, it must be a closed bracket
                if not stack:
                    # If currently empty and a closing bracket is found, its invalid so break immediately
                    return False
                else:
                    # Else, stack is not empty, so attempt to match the currently open bracket
                    if stack[-1] is not mappedBrackets.get(item):
                        return False
                    else:
                        # Match was found, pop the current item off stack and continue checking
                        stack.pop()

        # If the stack is not completely empty, the brackets were not closed
        if not stack:
            return True


if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()