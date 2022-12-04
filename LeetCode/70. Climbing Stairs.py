"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:
1 <= n <= 45

Hint: To reach nth step, what could have been your previous steps? (Think about the step sizes)
"""

from functools import lru_cache


class Solution:
    @lru_cache(maxsize=10)
    def climbStairs_rec(self, n: int) -> int:
        """Recursion with memoization. Top Down
        116 ns ± 4.98 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
        """
        if n in (0, 1, 2):
            return n
        return self.climbStairs_rec(n - 1) + self.climbStairs_rec(n - 2)

    def climbStairs_bottom_up1(self, n: int) -> int:
        """354 µs ± 30 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)"""
        if n in (0, 1, 2):
            return n
        result_dict = {1: 1, 2: 2}
        for i in range(3, n + 1):
            result_dict[i] = result_dict[i - 1] + result_dict[i - 2]
        return result_dict[n]

    def climbStairs_bottom_up2(self, n: int) -> int:
        """101 µs ± 2.54 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)"""
        if n in (0, 1, 2):
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            b, a = a + b, b
        return b


obj = Solution()
print(obj.climbStairs_rec(2))
print(obj.climbStairs_rec(3))
print(obj.climbStairs_rec(4))
print(obj.climbStairs_rec(5))
print(obj.climbStairs_rec(6))

print(obj.climbStairs_bottom_up2(2))
print(obj.climbStairs_bottom_up2(3))
print(obj.climbStairs_bottom_up2(4))
print(obj.climbStairs_bottom_up2(5))
print(obj.climbStairs_bottom_up2(6))
