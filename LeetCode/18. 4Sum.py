"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)

    def kSum(self, arr, target, k):
        # START: Base Case 1
        if not arr:
            return []
        # END: Base Case 1

        # START: Base Case 2
        '''There are k remaining values to add to the sum. The average of these values is at least target // k.
        We cannot obtain a sum of target if the smallest value in nums is greater than target // k or if the largest
        value in nums is smaller than target // k'''
        average_value = target // k
        if average_value < arr[0] or average_value > arr[-1]:
            return []
        # END: Base Case 2

        # START: Base Case 3
        if k == 2:
            return self.twoSum(arr, target)
        # END: Base Case 3

        result = []
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            k_minus_1_results = self.kSum(arr[i + 1:], target - arr[i], k - 1)
            for subset in k_minus_1_results:
                result.append([arr[i]] + subset)
        return result

    def twoSum(self, arr, target):
        result = []
        length = len(arr)
        left, right = 0, length - 1
        while left < right:
            current_sum = arr[left] + arr[right]
            if (current_sum < target) or (left > 0 and arr[left] == arr[left - 1]):
                left += 1
            elif (current_sum > target) or ((right < (length - 1)) and arr[right] == arr[right + 1]):
                right -= 1
            else:
                result.append([arr[left], arr[right]])
                left += 1
                right -= 1
        return result

    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     l = itertools.combinations(nums, 4)
    #     result = []
    #     for i in l:
    #         if sum(i) == target:
    #             result.append(list(i))
    #     return list(set(result))
