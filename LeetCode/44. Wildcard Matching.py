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
        # Clean up *'s
        while '**' in p:
            p = p.replace('**', '*')
        memoiz_dict = {}

        def rec_func(in_str, pattern):
            if (in_str, pattern) in memoiz_dict:
                return memoiz_dict[(in_str, pattern)]

            if (not in_str and not pattern) or (in_str == pattern) or (pattern == '*'):
                memoiz_dict[(in_str, pattern)] = True
                return True

            if not in_str or not pattern:
                memoiz_dict[(in_str, pattern)] = False
                return False

            s_idx, p_idx = 0, 0
            while s_idx < len(in_str) and p_idx < len(pattern):
                if pattern[p_idx] in ('?', in_str[s_idx]):
                    s_idx += 1
                    p_idx += 1
                elif pattern[p_idx] == '*':
                    result = rec_func(in_str[s_idx:], pattern[p_idx + 1:]) or \
                             rec_func(in_str[s_idx + 1:], pattern[p_idx:])
                    memoiz_dict[(in_str, pattern)] = result
                    return result
                else:
                    memoiz_dict[(in_str, pattern)] = False
                    return False
            if (s_idx < len(in_str)) or (p_idx < len(pattern) and pattern[p_idx:] != '*'):
                # print('p:', p)
                memoiz_dict[(in_str, pattern)] = False
                return False
            memoiz_dict[(in_str, pattern)] = True
            return True

        return rec_func(s, p)


obj = Solution()
print(obj.isMatch(s="aa", p="a"))  # False
print(obj.isMatch(s="aa", p="*"))  # True
print(obj.isMatch(s="cb", p="?a"))  # False
print(obj.isMatch(s="b", p="b*"))  # True
print(obj.isMatch(s="ab", p="?*"))  # True
print(obj.isMatch(s="mississippi", p="m??*ss*?i*pi"))  # False
print(obj.isMatch(s="ippi", p="*?i*pi"))  # False
print(obj.isMatch(s="pi", p="?i*pi"))  # False
print(obj.isMatch(s="", p="******"))  # True
