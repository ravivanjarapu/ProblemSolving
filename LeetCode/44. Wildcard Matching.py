"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.


Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if (not s and not p) or (s == p):
            return True
        # Clean up *'s
        p = p.replace('**', '*')
        if p == '*':
            return True

        if (len(s) < len(p)) or not s or not p:
            return False
        s_idx, p_idx = 0, 0
        while s_idx < len(s) and p_idx < len(p):
            if s[s_idx] in ('?', p[p_idx]):
                s_idx += 1
                p_idx += 1
            elif p[p_idx] == '*':
                return self.isMatch(s[s_idx:], p[p_idx + 1:]) or self.isMatch(s[s_idx + 1:], p[p_idx:])
            else:
                return False
        if (s_idx < len(s)) or (p_idx < len(p)):
            return False
        return True


obj = Solution()
print(obj.isMatch(s="aa", p="a"))
print(obj.isMatch(s="aa", p="*"))
print(obj.isMatch(s="cb", p="?a"))
