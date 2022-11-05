"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) in (0, 1, 2):
            return 0
        p, q = 0, len(height)-1
        result = 0
        left_max, right_max = 0, 0
        while p < q:
            # if left_max > height[p]:
            #     result += left_max - height[p]
            # if right_max > height[q]:
            #     result += right_max - height[q]
            #
            # left_max = max(left_max, height[p])
            # right_max = max(right_max, height[q])

            if height[p] <= height[q]:
                if left_max > height[p]:
                    result += left_max - height[p]
                else:
                    left_max = height[p]
                p += 1
            else:
                if right_max > height[q]:
                    result += right_max - height[q]
                else:
                    right_max = height[q]
                q -= 1
        return result


obj = Solution()
print(obj.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(obj.trap([4,2,0,3,2,5]))
