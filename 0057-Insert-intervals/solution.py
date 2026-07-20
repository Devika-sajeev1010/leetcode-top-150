class Solution(object):
    def insert(self, intervals, newInterval):
        ans = []

        for interval in intervals:

            # Case 1: current interval is completely before newInterval
            if interval[1] < newInterval[0]:
                ans.append(interval)

            # Case 2: current interval is completely after newInterval
            elif interval[0] > newInterval[1]:
                ans.append(newInterval)
                newInterval = interval

            # Case 3: overlap
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        ans.append(newInterval)

        return ans