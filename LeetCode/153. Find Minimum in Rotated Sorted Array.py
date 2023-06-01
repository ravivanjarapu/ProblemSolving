"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.


Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        LeetCode hints:
        1. Array was originally in ascending order. Now that the array is rotated, there would be a
        point in the array where there is a small deflection from the increasing sequence. eg. The array would be
        something like [4, 5, 6, 7, 0, 1, 2].

        2. You can divide the search space into two and see which direction to
        go. Can you think of an algorithm which has O(logN) search complexity?

        3. All the elements to the left of
        inflection point > first element of the array. All the elements to the right of inflection point < first
        element of the array.

        '''
        '''# https://www.youtube.com/watch?v=nIVW4P8b1VA   -   NeetCode
        # Complexity is good but not fast enough - Beats just 5.81%
        result = nums[0]  # at least one element is guaranteed as per constraints
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] <= nums[right]:  # This means array is in Ascending order
                return min(result, nums[left])
            mid = (left + right) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return result'''

        # Simpler code and simpler logic
        # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/158940/beat-100-very-simple-python-very-detailed-explanation/
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]   # This happens only when left = right


