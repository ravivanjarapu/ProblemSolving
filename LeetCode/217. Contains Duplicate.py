"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return True if len(set(nums)) < len(nums) else False
        # Worst case Time and space complexity of above is same as below. But in best and average cases, below is better
        # This is because we don't add all elements to set and return True as soon as we find duplicate
        visited = set()
        for i in nums:
            if i in visited:
                return True
            else:
                visited.add(i)
        return False
