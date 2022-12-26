"""
Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
from typing import List


class Solution:
    """ https://www.youtube.com/watch?v=REOH22Xwdkk"""

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, subset = [], []
        n = len(nums)

        def backtrack(idx=0):
            if idx >= n:
                result.append(subset.copy())
                return
            # to include the element
            subset.append(nums[idx])
            backtrack(idx + 1)

            # NOT to include the element
            subset.pop()
            backtrack(idx + 1)

        backtrack()
        return result


obj = Solution()
print(obj.subsets([1, 2, 3]))
