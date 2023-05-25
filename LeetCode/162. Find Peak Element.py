"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""
from typing import List
from unittest import TestCase, main


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """# This is O(n) time O(1) space solution
        current_peak = nums[0]
        result_index = 0
        for i, val in enumerate(nums[1:]):
            if val > current_peak:
                current_peak = val
                result_index = i + 1
            else:
                break
        return result_index
        # This is O(n) time O(1) space solution"""

        '''# O(log n) time and O( log n) space solution
        n = len(nums)
        if n == 1:
            return 0
        mid = n // 2
        if nums[mid-1] < nums[mid]:
            return mid + self.findPeakElement(nums[mid:])
        else:
            return self.findPeakElement(nums[:mid])

        # O(log n) time and O( log n) space solution'''

        # O(log n) time and O(1) space solution
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left
        # O(log n) time and O(1) space solution


class PeakTester(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.obj = Solution()

    def test1(self):
        self.assertEqual(self.obj.findPeakElement([1]), 0)

    def test2(self):
        self.assertEqual(self.obj.findPeakElement([1, 2, 1]), 1)

    def test3(self):
        self.assertEqual(self.obj.findPeakElement([1, 2, 3, 1]), 2)

    def test4(self):
        self.assertEqual(self.obj.findPeakElement([1, 2, 1, 3, 5, 6, 4]), 5)

    def test5(self):
        self.assertEqual(self.obj.findPeakElement([2,1]), 0)

    def test5(self):
        self.assertEqual(self.obj.findPeakElement([6,5,4,3,2,3,2]), 0)


if __name__ == "__main__":
    main()
