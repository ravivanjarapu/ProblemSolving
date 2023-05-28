"""Given four integer arrays nums1, nums2, nums3, and nums4 all the length n, return the number of tuples (i, j, k,l)
such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0


Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1


Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
"""
from typing import List, Tuple
from collections import Counter
from unittest import TestCase, main


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        # This is custom solution and correct for this question
        mediator = {}
        for i in nums1:
            for j in nums2:
                mediator[i + j] = mediator.get(i + j, 0) + 1

        result = 0
        for k in nums3:
            for m in nums4:
                result += mediator.get(-(k + m), 0)
        return result
        """

        # Below is generic solution for any number of arrays
        all_input_lists = [nums1, nums2, nums3, nums4]
        k = len(all_input_lists)

        left = self.generic_sum_count(all_input_lists[:k // 2])
        right = self.generic_sum_count(all_input_lists[k // 2:])

        return sum(left[key] * right.get(-key, 0) for key in left)  # for key in right is also fine

    @staticmethod
    def generic_sum_count(arrays: List[List[int]]) -> dict:
        """
        Take each element in each array, add the element to key of existing result and its count to existing result
        :param arrays:
        :return: dict of sums as keys and counts as values
        """

        result = {0: 1}
        # This is to ensure for loop on result is executed at least once. Value 1 is to ensure increment the count by 1
        # first time

        for arr in arrays:

            new_result = {}
            for i in arr:
                for total, count in result.items():
                    new_result[total + i] = new_result.get(total + i, 0) + count

            result = new_result
        return result


class FourSumTester(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obj = Solution()

    def test_example_1(self):
        nums1, nums2, nums3, nums4 = [1, 2], [-2, -1], [-1, 2], [0, 2]
        self.assertEqual(2, self.obj.fourSumCount(nums1, nums2, nums3, nums4))
        '''Output: 2
        Explanation:
        The two tuples are:
        1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
        2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0'''

    def test_example_2(self):
        nums1, nums2, nums3, nums4 = [0], [0], [0], [0]
        self.assertEqual(1, self.obj.fourSumCount(nums1, nums2, nums3, nums4))


if __name__ == '__main__':
    main()
