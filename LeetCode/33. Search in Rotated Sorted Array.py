"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        The idea is that we add some additional condition checks in the normal binary search in order to better narrow down the scope of the search.

        Algorithm

        As in the normal binary search, we keep two pointers (i.e. start and end) to track the search scope. At each iteration, we reduce the search scope into half, by moving either the start or end pointer to the middle (i.e. mid) of the previous search scope.

        Here are the detailed breakdowns of the algorithm:

        Initiate the pointer start to 0, and the pointer end to n - 1.

        Perform standard binary search. While start <= end:

        Take an index in the middle mid as a pivot.

        If nums[mid] == target, the job is done, return mid.

        Now there could be two situations:

        Pivot element is larger than the first element in the array, i.e. the subarray from the first element to the pivot is non-rotated, as shown in the following graph.
        pic

          - If the target is located in the non-rotated subarray:
          go left: `end = mid - 1`.

          - Otherwise: go right: `start = mid + 1`.
        Pivot element is smaller than the first element of the array, i.e. the rotation index is somewhere between 0 and mid. It implies that the sub-array from the pivot element to the last one is non-rotated, as shown in the following graph.
        pic

          - If the target is located in the non-rotated subarray:
          go right: `start = mid + 1`.

          - Otherwise: go left: `end = mid - 1`.
        We're here because the target is not found. Return -1.
        """
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1

        start, end = 0, n-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[end] >= target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


obj = Solution()
print(obj.search([4, 5, 6, 7, 0, 1, 2], 0))
print(obj.search([4, 5, 6, 7, 0, 1, 2], 3))
print(obj.search([3, 1], 1))
