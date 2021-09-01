# 32. Longest Valid Parentheses
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.


class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "longestValidParentheses"

    def defineTestCases(self):
        self.testCases.append("(()")
        #self.testCases.append(")()())")
        #self.testCases.append("(()())(()()())())()()")

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + case + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def longestValidParentheses(self, s: str) -> int:

        current_stack = []
        left_bracket_count = 0
        current_counter = 0
        max_counter = 0

        for bracket in s:
            print('current item:' + bracket)
            if bracket == '(':
                current_stack.append(s)
                left_bracket_count += 1
            else:
                if current_stack:
                    if current_stack[-1:] == '(':
                        current_counter += 2
                        current_stack.pop()
                        left_bracket_count -= 1

                        if current_counter > max_counter:
                            max_counter = current_counter

                    else:
                        # Count # of ), cannot exceed half stack:
                        if left_bracket_count > (len(current_stack) // 2):
                            current_stack = []
                            left_bracket_count = 0
                            current_counter = 0

                else:
                    # If empty stack, reset if )
                    current_stack = []
                    left_bracket_count = 0
                    current_counter = 0

        return max_counter


if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()