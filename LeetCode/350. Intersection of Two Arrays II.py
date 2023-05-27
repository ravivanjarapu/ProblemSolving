"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1):  # This is to ensure space complexity is limited to the smallest array size
            return self.intersect(nums2, nums1)

        # nums2_dict = dict(Counter(nums2))
        """
        nums2_dict = defaultdict(int)
        %timeit for i in nums2: nums2_dict[i] += 1
        621 ns ± 62.1 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
        
        %timeit dict(Counter(nums2))
        2.1 µs ± 223 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
        
        %timeit for i in nums2: nums2_dict[i] = nums2_dict.get(i, 0) + 1
        633 ns ± 55.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
        """
        nums2_dict = {}
        for i in nums2:
            nums2_dict[i] = nums2_dict.get(i, 0) + 1

        result = []
        for i in nums1:
            if i in nums2_dict and nums2_dict[i] > 0:
                result.append(i)
                nums2_dict[i] -= 1
        return result
