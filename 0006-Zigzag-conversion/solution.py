class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        ans = []
        cycle = 2 * numRows - 2

        for row in range(numRows):
            for j in range(row, len(s), cycle):
                ans.append(s[j])

                diagonal = j + cycle - 2 * row
                if row != 0 and row != numRows - 1 and diagonal < len(s):
                    ans.append(s[diagonal])

        return "".join(ans)
        