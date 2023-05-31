"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.



Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4


Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # https://www.youtube.com/watch?v=zx5Sw9130L0 - NeetCode
        max_area = 0
        stack = [(0, heights[0])]
        for curr_idx, val in enumerate(heights):
            if stack[-1][1] <= val:
                stack.append((curr_idx, val))
            else:
                while stack and stack[-1][1] > val:
                    last_idx, last_val = stack.pop()
                    max_area = max(max_area, (curr_idx-last_idx) * last_val)
                stack.append((last_idx, val))

        length = len(heights)
        while stack:
            last_idx, last_val = stack.pop()
            max_area = max(max_area, (length - last_idx) * last_val)
        return max_area


