"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.



Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1


Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row = 1
        rows, columns = len(matrix), len(matrix[0])
        for row_idx in range(rows):
            for col_idx in range(columns):
                if matrix[row_idx][col_idx] == 0:
                    matrix[0][col_idx] = 0
                    if row_idx == 0:
                        first_row = 0
                    else:
                        matrix[row_idx][0] = 0
        # for j in matrix:
        #     print(j)
        # print('first row: ', first_row)
        for row_idx in range(1, rows):
            for col_idx in range(1, columns):
                if (matrix[row_idx][0] == 0) or (matrix[0][col_idx] == 0):
                    matrix[row_idx][col_idx] = 0

        # Can change below to list comprehension also
        if matrix[0][0] == 0:
            for row_idx in range(rows):
                matrix[row_idx][0] = 0
        if first_row == 0:
            for col_idx in range(columns):
                matrix[0][col_idx] = 0



obj = Solution()
mtx = [[1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]]
# mtx = [[0, 1, 2, 0],
#        [3, 4, 5, 2],
#        [1, 3, 1, 5]]
obj.setZeroes(mtx)
print('********')
for i in mtx:
    print(i)
