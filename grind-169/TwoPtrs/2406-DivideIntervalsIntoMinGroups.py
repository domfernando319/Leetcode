class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        '''
        Visually overlay intervals on a number lines. See the 
        relationship between the start and end points and the interval.
        Use a line to scan through intervals and count max number of 
        overlay intervals at a time for the entire range.
        that max is your answer

        Time: O(n) + O(nlogn) + O(n) -> O(nlogn) The sorting dominates where n is the len(intervals)
        Space: O(n) you need two arrays of size n to store the 
        start values and the end values
        '''
        res = 0
        startPts, endPts = [], []
        # O(n)
        for left, right in intervals:
            startPts.append(left)
            endPts.append(right)

        # sorting takes O(nlogn)
        startPts.sort()
        endPts.sort()
        print(startPts, endPts)

        # begin two pointers traversal O(n)
        startPtr = 0
        endPtr = 0
        numGroups = 0

        while startPtr < len(intervals):
            if startPts[startPtr] <= endPts[endPtr]:
                startPtr += 1
                numGroups += 1
            else:
                endPtr += 1
                numGroups -= 1
            res = max(res, numGroups)

        return res


