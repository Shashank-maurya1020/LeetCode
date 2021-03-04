# https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        for i in range(len(s)):
            temp = []
            for j in range(i, len(s)):
                if s[j] not in set(temp):
                    temp += [s[j]]
                    if len(temp) > max_l:
                        max_l = len(temp)
                else:
                    break
        return max_l