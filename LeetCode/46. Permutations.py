"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) in (0, 1):
            return [nums]
        elif len(nums) == 2:
            return [nums, [nums[1], nums[0]]]
        else:
            result = []
            for i in range(len(nums)):
                smaller_list = nums[:i] + nums[i+1:]
                for j in self.permute(smaller_list):
                    result.append([nums[i]] + j)
            return result


if __name__ == '__main__':
    obj = Solution()
    nums = [1, 2, 3]
    nums = [1, 2, 3, 4]
    # nums = [0,1]
    nums = [1]
    for i in obj.permute(nums):
        print(i)
