# 33. Search in Rotated Sorted Array

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "search"

    def defineTestCases(self):
        #self.testCases.append([[5, 6, 2, 3, 4], 3])
        #self.testCases.append([[6, 7, 1, 2, 3, 4, 5], 7])
        self.testCases.append([[1, 2, 3, 4, 5, 6, 7, 0], 5])
        self.testCases.append([[2, 3, 4, 5, 6, 7, 0, 1], 5])
        self.testCases.append([[1, 2, 3, 4, 5, 6, 7, 0], -1])
        #self.testCases.append([[1, 4, 7, 8], 5])
        #self.testCases.append([[-1, 0, 4, 7], 4])
        #self.testCases.append([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 12])
        #self.testCases.append(([[0, 1, 2, 2, 3, 0, 4, 2], 2]))
        #self.testCases.append([[3, 3], 3])
        #self.testCases.append([[3, 3, 3, 3], 3])
        #self.testCases.append([[2], 3])
        #self.testCases.append([[3, 2, 2, 3], 3])

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case[0], case[1])))

    def search(self, nums: List[int], target: int) -> int:

        # Find the pivot point where nums[i] > nums[i+1]
        # Use binary search to cut the array until found
        # [1,2,3,4,5,6,7,0]
        # [7,0,1,2,3,4,5,6]
        # [4,5,1,2,3]

        clone = nums
        pos = 0
        while len(clone) > 2:
            mid = len(clone)//2 -1

            # Check if pivot is mid, break if found, else
            if clone[mid] > clone[mid+1]:
                clone = [clone[mid]]
                pos = pos + mid
                break

            # [1,2,3,4|5,6,7,0]
            # If right[end] < right[start], then the pivot is on the right side, else left
            # In case of right side, add the midpoint to the position

            if clone[-1] < clone[mid+1]:
                clone = clone[mid+1:]
                pos = pos + mid + 1
            else:
                clone = clone[:mid+1]

#            pos += mid

        # Stop case - if 2 items remain,
        if len(clone) == 2 and clone[0] > clone[1]:
            #pos += 1
            pass

        itemPos = 0
        if target >= nums[0] and target <= nums[pos]:
            # Search in left half
            clone = nums[:pos+1]
            print("Target in left half, searching in:" + str(clone))
            itemPos = self.binary_search(clone, target)
            pass
        else:
            # Search in right half if item < start
            clone = nums[pos+1:]
            print("Target in right half, searching in:" + str(clone))

            itemPos = self.binary_search(clone, target)
            if itemPos >= 0:
                itemPos += pos + 1

        print("Pivot is:" + str(pos) + ", item at pivot:" + str(nums[pos]))
        return itemPos

    # Copied binary search code off internet
    def binary_search(self, arr, x):
        low = 0
        high = len(arr) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2
            # If x is greater, ignore left half
            if arr[mid] < x:
                low = mid + 1
            # If x is smaller, ignore right half
            elif arr[mid] > x:
                high = mid - 1
            # means x is present at mid
            else:
                return mid

        # If we reach here, then the element was not present
        return -1

if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()