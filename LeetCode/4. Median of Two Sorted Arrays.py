'''
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # OWN LOGIC - O((m+n)/2) time and O((m+n)/2) space complexity
        i, j = 0, 0
        merged_array = []
        m, n = len(nums1), len(nums2)
        total = m + n
        median_indices = [(total - 1) // 2]
        even = False
        if total % 2 == 0:
            even = True
            median_indices.append(median_indices[-1] + 1)
        break_length = median_indices[-1] + 1

        while (len(merged_array) < break_length) and (i < m or j < n):
            if i == m:
                merged_array.append(nums2[j])
                j += 1
            elif j == n:
                merged_array.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                merged_array.append(nums1[i])
                i += 1
            else:
                merged_array.append(nums2[j])
                j += 1
        if even:
            return (merged_array[-1] + merged_array[-2]) / 2
        return merged_array[-1]

