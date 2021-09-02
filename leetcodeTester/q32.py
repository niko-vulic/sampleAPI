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
        #self.testCases.append("(()")
        #self.testCases.append(")()())")
        #self.testCases.append("()(()")
        #self.testCases.append("(()())(()()")
        self.testCases.append("()(())")
        #self.testCases.append(")()())")
        self.testCases.append("(()())")


    def runTests(self):
        for case in self.testCases:
            print("Test case:" + case + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def longestValidParentheses(self, s: str) -> int:

        # Approach with DP
        dp_array = [0] * len(s)
        max_counter = 0

        # Init the first two elements of dp array to make following code simpler
        if len(s) >= 2 and s[0] == '(' and s[1] == ')':
            dp_array[1] = 2
            max_counter = 2

        for i in range(2, len(s)):
            # Track only on closed brackets
            #print("Checking element " + str(i) + ", value:" + str(s[i]) + " of string " + s)

            if s[i] == ')':
                # Valid parenthesis in 2 cases - either () extends sequence or )) and check prior location of )
                current_seq = 0

                # Simple case of ()
                if s[i - 1] == '(':
                    current_seq = 2
                else:
                    # Check for cases of )), not caught by simple case
                    if dp_array[i-1] > 0:
                        prior_index = i - dp_array[i-1] - 1
                        #print("Case of )) for index:" + str(i) + ",checking prior index:" + str(prior_index))
                        # Ensure prior_index > 0, else python wraps the array and ())( = 4
                        if prior_index >= 0 and s[prior_index] == '(':
                            current_seq = dp_array[i - 1] + 2

                # In both scenarios, we check if we can append to an existing sequence
                if current_seq > 0:
                    prior_valid_seq = i - current_seq
                    #print("Case of ))+_, summing current value:" + str(dp_array[i]) + " with prior index:" + str(prior_valid_seq))
                    # If s[1+] already has a sequence, append the count
                    if prior_valid_seq > 0:
                        dp_array[i] = current_seq + dp_array[prior_valid_seq]
                    else:
                        dp_array[i] = current_seq


                if dp_array[i] > max_counter:
                    max_counter = dp_array[i]
            #print("Current dp array:" + str(dp_array))

        return max_counter

    def longestValidParentheses_backup(self, s: str) -> int:

        # Approach with DP
        dp_array = [0] * len(s)
        max_counter = 0

        # Init the first two elements of dp array to make following code simpler
        if len(s) >= 2 and s[0] == '(' and s[1] == ')':
            dp_array[1] = 2
            max_counter = 2

        for i in range(2, len(s)):
            # Track only on closed brackets
            #print("Checking element " + str(i) + ", value:" + str(s[:i+1]) + " of string " + s)

            if s[i] == ')':
                # Check the stopping simple case of ()
                if s[i-1] == '(':
                    # For the simple () case, check if a sequence is already being tracked and append to it:
                    if dp_array[i-2] == 0:
                        dp_array[i] = dp_array[i-2] + 2
                    else:
                        dp_array[i] = 2
                else:
                    # If the prior array item is not () simple case, check to see if a sequence is already underway
                    if dp_array[i-1] > 0:
                        prior_element_to_check = i - dp_array[i-1] -1
                        #if prior_element_to_check > 0:
                        if s[prior_element_to_check] == '(':
                            dp_array[i] = dp_array[i-1] + 2

                if dp_array[i] > max_counter:
                    max_counter = dp_array[i]
            print("Current dp array:" + str(dp_array))

        return max_counter

    def longestValidParentheses_failed_answer(self, s: str) -> int:

        current_stack = []
        left_bracket_count = 0
        current_counter = 0
        max_counter = 0

        for bracket in s:
            #print('current item:' + bracket)
            if bracket == '(':
                current_stack.append(bracket)
                left_bracket_count += 1
            else:
                if current_stack:
                    #print('Stack exists, checking last item' + current_stack[-1])
                    if current_stack[-1] == '(':
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