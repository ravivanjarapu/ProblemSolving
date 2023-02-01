"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To
accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109


Follow up: Can you come up with an algorithm that runs in O(m + n) time?
Hint (1/2) You can easily solve this problem
if you simply think about two elements at a time rather than two arrays. We know that each of the individual arrays
is sorted. What we don't know is how they will intertwine. Can we take a local decision and arrive at an optimal
solution?
Hint (2/2) If you simply consider one element each at a time from the two arrays and make a decision and
proceed accordingly, you will arrive at the optimal solution.
"""
from typing import List
from unittest import TestCase, main


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p, q, filler = m - 1, n - 1, m + n - 1
        while p >= 0 and q >= 0:
            if nums1[p] <= nums2[q]:
                nums1[filler] = nums2[q]
                q -= 1
            else:
                nums1[filler] = nums1[p]
                p -= 1
            filler -= 1
        if p < 0 and q >= 0:
            for i in range(q + 1):
                nums1[i] = nums2[i]
        # if m == 0 and n > m:
        #     for i in range(len(nums1)):
        #         nums1[i] = nums2[i]
        #     return


class SimpleTest(TestCase):
    @classmethod
    def setUpClass(cls):
        # print("setUpClass")
        cls.obj = Solution()

    def test1(self):
        a = [1, 2, 3, 0, 0, 0]
        self.obj.merge(a, 3, [2, 5, 6], 3)
        self.assertEqual(a, [1, 2, 2, 3, 5, 6])

    def test2(self):
        a = [1]
        self.obj.merge(a, 1, [], 0)
        self.assertEqual(a, [1])

    def test3(self):
        a = [0]
        self.obj.merge(a, 0, [1], 1)
        self.assertEqual(a, [1])

    def test4(self):
        a = [2, 0]
        self.obj.merge(a, 1, [1], 1)
        self.assertEqual(a, [1, 2])

    # def test2(self):
    #     self.assertNotEqual(5 * 2, 10)

    # def test3(self):
    #     self.assertTrue(4 + 5 == 9, "The result is False")

    # def test4(self):
    #     self.assertTrue(4 + 5 == 10, "assertion fails")

    # def test5(self):
    #     self.assertIn(3, [1, 2, 3])

    # def test6(self):
    #     self.assertNotIn(3, range(5))


if __name__ == '__main__':
    main()
