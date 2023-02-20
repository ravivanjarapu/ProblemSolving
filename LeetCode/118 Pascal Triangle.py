"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
"""
from typing import List
from unittest import TestCase, main


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        if numRows > 0:
            result.append([1])
        for i in range(1, numRows):
            sub_result = [1]
            for j in range(1, i):
                sub_result.append(result[i - 1][j - 1] + result[i - 1][j])
            sub_result.append(1)
            result.append(sub_result)
        print("result: ", result)
        return result


class PascalTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obj = Solution()

    def test1(self):
        self.assertEqual(self.obj.generate(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])


if __name__ == '__main__':
    main()
