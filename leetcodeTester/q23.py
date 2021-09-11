# 23. Merge k Sorted Lists

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# import math
import bisect
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        stringRepr = 'ListNode:[' + str(self.val)
        temp = self.next
        while temp:
            stringRepr = stringRepr + ',' + str(temp.val)
            temp = temp.next
        return stringRepr + ']'

    #def __lt__(self, other):
    #    return (self.val < other.val)

    #def __le__(self, other):
    #    return (self.val <= other.val)

class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "mergeKLists"

    def defineTestCases(self):
        listOne = ListNode(0, ListNode(1, ListNode(2)))
        listTwo = ListNode(2, ListNode(3, ListNode(4)))
        #self.testCases.append([listTwo, listOne])
        # Test Case Two - LC - [[1,4,5],[1,3,4],[2,6]]
        l3 = ListNode(1, ListNode(4, ListNode(5)))
        l4 = ListNode(1, ListNode(3, ListNode(4)))
        l5 = ListNode(2, ListNode(6))
        self.testCases.append([l3,l4,l5])
        self.testCases.append([])

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        while None in lists: lists.remove(None)

        head = ListNode(-1)
        curr = head

        # print("0 element:" +str(lists[0]))
        # Sort the list first so we can do log n operations based on the min size
        lists.sort(key=lambda ln: ln.val)

        while lists:
            # Elements will always be removed and re-inserted
            temp = lists.pop(0)
            tempNode = ListNode(temp.val)
            curr.next = tempNode
            curr = curr.next

            if temp.next:
                insertIndex = self.binary_search_ListNode(lists, temp.next)
                lists.insert(insertIndex, temp.next)
                # bisect.insort(lists, temp.next)

        # print("Final result:" + str(head.next))
        return head.next

    # Copied binary search code off internet
    def binary_search_ListNode(self, arr, x):
        if len(arr) == 0:
            return 0

        low = 0
        high = len(arr) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2
            # If x is greater, ignore left half
            if arr[mid].val < x.val:
                low = mid + 1
            # If x is smaller, ignore right half
            elif arr[mid].val > x.val:
                high = mid - 1
            # means x is present at mid
            else:
                return mid

        # If we reach here, then the element was not present
        # return -1
        if x.val < arr[mid].val:
            return mid
        else:
            return mid + 1




if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()