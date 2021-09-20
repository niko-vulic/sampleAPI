# 1014. Best Sightseeing Pair

# You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.
# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.
# Return the maximum score of a pair of sightseeing spots.

from typing import List


class Solution:
    def __init__(self):
        self.testCases = []
        self.funcName = "maxScoreSightseeingPair"

    def defineTestCases(self):
        self.testCases.append([0, 1, 2])
        self.testCases.append([8, 1, 5, 2, 6])
        self.testCases.append([10, 1, 1, 1, 1, 1, 7, 1, 8, 1, 1, 1, 1, 1, 1, 10])
        self.testCases.append([1, 3, 5])

    def runTests(self):
        for case in self.testCases:
            print("Test case:" + str(case) + ", answer is:" + str(getattr(self, self.funcName)(case)))

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        print(values)

        valueIfI = [0] * len(values)
        valueIfJ = [0] * len(values)
        maxCurr = [0] * len(values)

        maxValue = 0

        valueIfI[0] = values[0]
        maxCurr[0] = values[0]

        # Get the best sightseeting value first - max i + values[i]
        for i in range(1, len(values)):
            valueIfI[i] = values[i] + i
            valueIfJ[i] = values[i] - i
            # maxCurr[i] = valueIfJ[i] + max(maxCurr[i-1], valueIfI[i-1])
            maxCurr[i] = max(maxCurr[i - 1], values[i-1] + i-1)

            localMax = values[i] - i + maxCurr[i]
            if localMax > maxValue:
                maxValue = localMax

        print('Values of spots if i: ' + str(valueIfI))
        print('Values of spots if j: ' + str(valueIfJ))
        print('Final max is:' + str(maxValue))

        return maxValue

    def maxScoreSightseeingPairWorkingPreOptimized(self, values: List[int]) -> int:
        print(values)

        valueIfI = [0] * len(values)
        valueIfJ = [0] * len(values)
        maxCurr = [0] * len(values)

        maxValue = 0

        valueIfI[0] = values[0]
        maxCurr[0] = values[0]

        # Get the best sightseeting value first - max i + values[i]
        for i in range(1, len(values)):
            valueIfI[i] = values[i] + i
            valueIfJ[i] = values[i] - i
            # maxCurr[i] = valueIfJ[i] + max(maxCurr[i-1], valueIfI[i-1])
            maxCurr[i] = max(maxCurr[i - 1], valueIfI[i - 1])

            if valueIfJ[i] + maxCurr[i] > maxValue:
                maxValue = valueIfJ[i] + maxCurr[i]

        print('Values of spots if i: ' + str(valueIfI))
        print('Values of spots if j: ' + str(valueIfJ))
        print('Final max is:' + str(maxValue))

        return maxValue


if __name__ == '__main__':
    soln = Solution()
    soln.defineTestCases()
    soln.runTests()
