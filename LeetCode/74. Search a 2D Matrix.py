"""
You are given an m x n integer matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
from typing import List
from unittest import TestCase, main


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        left, right = 0, (rows*columns) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid//columns][mid % columns]  # This is the trick of matrices to remember
            if mid_value < target:
                left = mid + 1
            elif mid_value > target:
                right = mid - 1
            else:
                return True
        return False


class SearchMatrixTester(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.obj = Solution()

    def test_search_matrix(self):
        self.assertEqual(self.obj.searchMatrix(
            matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            target=3),
            True)
        self.assertEqual(self.obj.searchMatrix(
            matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            target=13),
            False)


if __name__ == '__main__':
    main()
