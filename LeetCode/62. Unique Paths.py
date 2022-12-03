"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.



Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


Constraints:

1 <= m, n <= 100
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1] * n for _ in range(m)]
        # matrix[0] = [1]*n
        # for i in matrix:
        #     print(i)
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
                # print('i: {0}, j: {1}, matrix: {2}'.format(i, j, matrix))
        return matrix[m - 1][n - 1]


obj = Solution()
print(obj.uniquePaths(m=3, n=7))  # Output: 28
print(obj.uniquePaths(m=3, n=2))  # Output: 3
print(obj.uniquePaths(m=3, n=1))  # Output: 1
