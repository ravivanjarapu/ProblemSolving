"""You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of
the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right
by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()

        left, right = 0, 0
        length = len(nums)
        result = []
        while right < length:
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)  # Add right to window

            if left > q[0]:  # Remove left from window. if index at q[0] is less than left, it is out of window
                q.popleft()

            # since we started from right=0, we should skip at least k elements to start appending to output
            if (right + 1) >= k:
                result.append(nums[q[0]])
                left += 1
            right += 1

        return result
