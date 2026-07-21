class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0

        # Sort by end coordinate
        points.sort(key=lambda x: x[1])

        arrows = 1
        arrowPos = points[0][1]

        for start, end in points[1:]:
            if start > arrowPos:
                arrows += 1
                arrowPos = end

        return arrows