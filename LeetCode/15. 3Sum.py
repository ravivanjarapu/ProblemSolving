"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set = set()
        if len(nums) < 3:
            return []
        # # Using three pointers - Didn't work
        # i, j, k = 0, 1, 2
        # while len(nums) > k > j > i:
        #     sum_value = nums[i] + nums[j] + nums[k]
        #     if sum_value == 0:
        #         result_set.add((nums[i], nums[j], nums[k]))
        #         i += 1
        #         j += 1
        #         k += 1
        #     elif sum_value < 0:
        #         min_value = min(nums[i], nums[j], nums[k])
        #         if nums[i] == min_value:
        #             i += 1
        #         elif nums[j] == min_value:
        #             j += 1
        #         else:
        #             k += 1
        #     else:
        #         max_value = max(nums[i], nums[j], nums[k])
        #         if nums[i] == max_value:
        #             i += 1
        #         elif nums[j] == max_value:
        #             j += 1
        #         else:
        #             k += 1
        # return list(result_set)
        # Using the solution from Two Sum problem
        for i_idx, i in enumerate(nums):
            target_value = 0 - i
            go_to_next = False
            for j_idx, j in enumerate(nums[i_idx + 1:]):
                k = target_value - j
                hash_set = set(nums[j_idx + 1:])
                if k in hash_set:
                    result_set.add(tuple(sorted((i, j, k))))
                    go_to_next = True
                    break

            if go_to_next:
                continue
        return [list(i) for i in result_set]


obj = Solution()
nums = [-1, 0, 1, 2, -1, -4]
nums = [0, 1, 1]
nums = [0, 0, 0]
print(obj.threeSum(nums))
