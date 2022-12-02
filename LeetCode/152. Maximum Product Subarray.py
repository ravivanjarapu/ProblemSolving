'''
Given an integer array nums, find a
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result, maxP, minP = nums[0], nums[0], nums[0]
        for i in nums[1:]:
            maxP, minP = max(maxP * i, i, minP * i), min(maxP * i, i, minP * i)
            result = max(result, maxP)

        return result


obj = Solution()
input_nums = [2, 3, -2, 4]  # 6
input_nums = [-2, 0, -1]  # 0
input_nums = [-2, 0, 1]  # 1
input_nums = [3, -1, 4]  # 4
input_nums = [2, -5, -2, -4, 3]  # 24
print(obj.maxProduct(input_nums))
