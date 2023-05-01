"""Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
from typing import List
from unittest import TestCase, main


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for idx in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if s[idx:idx + len(w)] == w:
                    dp[idx] = dp[idx + len(w)]
                if dp[idx]:
                    break
        return dp[0]


class WordBreakTester(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.obj = Solution()

    def test_1(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        self.assertEqual(self.obj.wordBreak(s, wordDict), True)

    def test_2(self):
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        self.assertEqual(self.obj.wordBreak(s, wordDict), True)

    def test_3(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        self.assertEqual(self.obj.wordBreak(s, wordDict), False)


if __name__ == "__main__":
    main()
