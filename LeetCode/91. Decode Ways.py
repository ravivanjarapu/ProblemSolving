"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.



Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").


Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""
from itertools import combinations
from unittest import TestCase, main


class Solution:
    def numDecodings(self, s: str) -> int:
        """https: // www.youtube.com / watch?v = o1i7JYWbwOE"""
        # for i, j in combinations(range(len(stuff) + 1), 2):
        #     print(stuff[i:j])
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        two_back, one_back = 1, 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != '0':
                current = one_back
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                current += two_back
            two_back, one_back = one_back, current
        return one_back


class SimpleTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obj = Solution()

    def test1(self):
        self.assertEqual(self.obj.numDecodings("12"), 2)

    def test2(self):
        self.assertEqual(self.obj.numDecodings("226"), 3)

    def test3(self):
        self.assertEqual(self.obj.numDecodings("06"), 0)

    def test4(self):
        self.assertEqual(self.obj.numDecodings("11106"), 2)


if __name__ == '__main__':
    main()
