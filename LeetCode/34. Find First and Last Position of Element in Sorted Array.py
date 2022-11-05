"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []

        def recursion_helper(lst, previous=0):
            if len(lst) == 1 and lst[0] == target:
                result.append(previous)
            elif len(lst) > 1:
                mid = (len(lst) // 2) - 1
                if lst[mid] == target:
                    result.append(mid + previous)
                    if lst[0] == target:
                        result.append(previous)
                    elif lst[mid - 1] == target:
                        recursion_helper(lst[:mid], previous)

                    if lst[-1] == target:
                        result.append(len(lst) - 1 + previous)
                    elif lst[mid + 1] == target:
                        recursion_helper(lst[mid + 1:], previous=previous + mid + 1)
                elif lst[mid] < target:
                    recursion_helper(lst[mid + 1:], previous=previous + mid + 1)
                else:
                    recursion_helper(lst[:mid], previous)

        recursion_helper(nums)
        if len(result) == 0:
            return [-1, -1]
        else:
            return [min(result), max(result)]
