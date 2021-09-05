# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "addTwoNumbers"

    def defineTestCases(self):
        #
        # l1 = 1,2,3
        l3 = ListNode(3)
        l2 = ListNode(2, l3)
        l1 = ListNode(1, l2)
        # l4 = 4,7,7
        l6 = ListNode(7)
        l5 = ListNode(7, l6)
        l4 = ListNode(4, l5)
        # la_3 = 2,4,3
        la_1 = ListNode(3)
        la_2 = ListNode(4, la_1)
        la_3 = ListNode(2, la_2)
        # la_6 = 5,6,4
        la_4 = ListNode(4)
        la_5 = ListNode(6, la_4)
        la_6 = ListNode(5, la_5)

        self.testCases.append([l1, l4])
        self.testCases.append([la_3, la_6])
        self.testCases.append([l1, la_6])


    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case[0], case[1])))

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        l1_reversed = []
        while l1:
            temp = l1.val
            l1_reversed.insert(0, temp)
            l1 = l1.next

        l2_reversed = []
        while l2:
            temp = l2.val
            l2_reversed.insert(0, temp)
            l2 = l2.next

        lt = []
        remainder = 0

        while l1_reversed or l2_reversed:
            temp = remainder
            if l1_reversed:
                temp += l1_reversed.pop()
            if l2_reversed:
                temp += l2_reversed.pop()
            remainder = 0

            # Check to see if there is a remainder
            if temp > 9:
                temp -= 10
                remainder = 1
            lt.append(temp)

        if remainder > 0:
            lt.append((remainder))

        tail = ListNode(lt.pop())
        while lt:
            currentNode = ListNode(lt.pop(), tail)
            tail = currentNode
        return tail


    def addTwoNumbers_pre_optimized(self, l1: ListNode, l2: ListNode) -> ListNode:

        l1_reversed = []
        while l1:
            temp = l1.val
            l1_reversed.insert(0, temp)
            l1 = l1.next
        print("L1 :" + str(l1_reversed))

        l2_reversed = []
        while l2:
            temp = l2.val
            l2_reversed.insert(0, temp)
            l2 = l2.next
        print("L2 :" + str(l2_reversed))

        lt = []
        remainder = 0

        while l1_reversed and l2_reversed:
            temp = l1_reversed[-1] + l2_reversed[-1] + remainder
            remainder = 0

            # Check to see if there is a remainder
            if temp > 9:
                temp -= 10
                remainder = 1

            lt.append(temp)
            l1_reversed.pop()
            l2_reversed.pop()


        print("Current LT:" + str(lt))
        print("Remaining size of list1:" + str(len(l1_reversed)))
        print("Remaining size of list2:" + str(len(l2_reversed)))

        while l1_reversed:
            temp = l1_reversed[-1] + remainder
            remainder = 0

            # Check to see if there is a remainder
            if temp > 9:
                temp -= 10
                remainder = 1

            lt.append(temp)
            l1_reversed.pop()

        while l2_reversed:
            temp = l2_reversed[-1] + remainder
            remainder = 0

            # Check to see if there is a remainder
            if temp > 9:
                temp -= 10
                remainder = 1

            lt.append(temp)
            l2_reversed.pop()


        if remainder > 0:
            lt.append((remainder))

        print("Final result:" + str(lt))


        tail = ListNode(lt.pop())
        while lt:
            currentNode = ListNode(lt.pop(), tail)
            tail = currentNode

        return tail


if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()