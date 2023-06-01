#Leetcode 435
# Runtime: O(nlogn) where n = the # of elements(intervals)
# Space complexity: O(n), where n = # of elements in result array


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort(key = lambda i:i[0])
        output = [intervals[0]]

        for x,y in intervals[1:]:
            lasty = output[-1][1]
            if x < lasty:
                output[-1][1] = min(y,lasty)
                result += 1
            else:
                output.append([x,y])
        print(output)
        return result