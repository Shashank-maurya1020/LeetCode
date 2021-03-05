# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def is_palindrome(self, s: str) -> bool:
        if len(s) % 2 == 0:
            return s[:len(s) // 2] == s[len(s) // 2:][::-1]
        return s[:len(s) // 2] == s[len(s) // 2 + 1:][::-1]
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 2:
            if s[0]==s[1]:
                return s
            return s[0]
        pal_s = s[0]
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if len(s[i:j+1]) > len(pal_s):
                        if self.is_palindrome(s[i:j+1]):
                            pal_s = s[i:j + 1]
        return pal_s