"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


from unittest import TestCase, main


class Solution:
    '''
    LC Hint:
    1. Obviously, brute force will result in TLE. Think of something else.
    2. How will you check whether one string is a permutation of another string?
    3. One way is to sort the string and then compare. But, Is there a better way?
    4. If one string is a permutation of another string then they must one common metric. What is that?
    5. Both strings must have same character frequencies, if one is permutation of another. Which data structure
    should be used to store frequencies?
    6. What about hash table? An array of size 26?
    '''

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) >= len(s1):
            s1_counter, s2_counter = {}, {}

            for ascii_value in range(97, 123):  # a-z
                s1_counter[chr(ascii_value)] = 0  # Convert ASCII value to character
                s2_counter[chr(ascii_value)] = 0

            for i in range(len(s1)):
                s1_counter[s1[i]] += 1
                s2_counter[s2[i]] += 1

            matches = 0
            for alphabet, s1_count in s1_counter.items():
                if s2_counter[alphabet] == s1_count:
                    matches += 1

            left = 0
            for right in range(len(s1), len(s2)):
                if matches == 26:
                    return True

                alphabet = s2[right]
                if s1_counter[alphabet] == s2_counter[alphabet]:
                    matches -= 1  # If its matching earlier, we are disturbing it since we are incrementing in next line

                s2_counter[alphabet] += 1
                if s1_counter[alphabet] == s2_counter[alphabet]:
                    matches += 1

                alphabet = s2[left]  # We will now remove this from sliding window since we added one letter above
                if s1_counter[alphabet] == s2_counter[alphabet]:
                    matches -= 1

                s2_counter[alphabet] -= 1
                if s1_counter[alphabet] == s2_counter[alphabet]:
                    matches += 1

                left += 1
            return matches == 26

        return False


class CheckInclusionTester(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.obj = Solution()

    def test_check_inclusion(self):
        self.assertEqual(True,
                         self.obj.checkInclusion("ab", "eidbaooo"))

        self.assertEqual(False,
                         self.obj.checkInclusion("ab", "eidboaoo"))

if __name__ == "__main__":
    main()