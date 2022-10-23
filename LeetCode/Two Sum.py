'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.'''
from big_o import big_o


class Solution:
    # O(n^2)
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     for idx, val in enumerate(nums):  # O(n)
    #         second_num = target - val
    #         if second_num in nums[idx + 1:]:  # O(n)
    #             return [idx, nums[idx + 1:].index(second_num) + idx + 1]

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for idx, val in enumerate(nums):
            d[val] = idx

        for idx, val in enumerate(nums):  # O(n)
            second_num = target - val
            if second_num in d and d[second_num] != idx:  # O(1)
                return [idx, d[second_num]]


print(Solution().twoSum([1, 3, 5, 7, 8], 8))
