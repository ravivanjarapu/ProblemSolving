"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) in (0, 1):
            return 0
        p, q = 0, 1
        result = 0
        while q < len(height):
            print('p, q: ', p, q)
            result = max(result, (min(height[p], height[q]) * (q - p)))
            print('result: ', result, '\n')
            if height[p] < height[q]:
                p = q
            q += 1
        return result


obj = Solution()
# print(obj.maxArea([1, 2, 3, 4, 5, 6, 7]))
# print(obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(obj.maxArea([1, 1]))
