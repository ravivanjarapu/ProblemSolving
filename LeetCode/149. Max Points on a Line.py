"""Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number
of points that lie on the same straight line.



Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4


Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""
from typing import List
from collections import defaultdict
from unittest import TestCase, main


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        result = 1  # Since 1 <= points.length <= 300, at least 1 point is expected
        for i, p1 in enumerate(points):
            # Same reason as above. Since we are taking i as reference, we have at least 1 point
            counter_dict = defaultdict(int)

            for p2 in points[i + 1:]:

                slope = float('inf') if p1[0] == p2[0] else (p2[1] - p1[1]) / (p2[0] - p1[0])
                counter_dict[slope] += 1
                result = max(counter_dict[slope] + 1, result)
        return result


class MaxPointsTester(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.obj = Solution()

    def test1(self):
        points = [[1, 1], [2, 2], [3, 3]]

        self.assertEqual(self.obj.maxPoints(points), 3)

    def test2(self):
        points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]

        self.assertEqual(self.obj.maxPoints(points), 4)


if __name__ == "__main__":
    main()
