"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] == 1:
                return 2
            else:
                return 1
        print('\nnums before: ', nums)
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        print('nums after filling -ve: ', nums)
        for i in range(len(nums)):
            if 0 < abs(nums[i]) <= len(nums):
                target_index = abs(nums[i]) - 1
                if nums[target_index] == 0:
                    nums[target_index] = -abs(nums[i])
                elif nums[target_index] > 0:
                    nums[target_index] = -nums[target_index]
        print('nums after marking available: ', nums)

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1


obj = Solution()
print(obj.firstMissingPositive([1, 2, 0]))
print(obj.firstMissingPositive([3, 4, -1, 1]))
print(obj.firstMissingPositive([7, 8, 9, 11, 12]))
print(obj.firstMissingPositive([1]))
print(obj.firstMissingPositive([]))
print(obj.firstMissingPositive([-1, -2]))
print(obj.firstMissingPositive([2, 1]))
print(obj.firstMissingPositive([2, 2]))
print(obj.firstMissingPositive([-1, 4, 2, 1, 9, 10]))
