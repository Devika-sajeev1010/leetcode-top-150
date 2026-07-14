class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None
        """
        m = len(matrix)
        n = len(matrix[0])

        first_col = False

        # Step 1: Mark rows and columns
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True

            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 2: Fill the inner matrix
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: First row
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        # Step 4: First column
        if first_col:
            for i in range(m):
                matrix[i][0] = 0