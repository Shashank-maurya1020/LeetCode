# https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''
# solution 1: O(n^2)
class Solution_1:
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

# Solution 2: O(n)
class Solution_2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        di = dict()
        max_l = 0
        j = 0
        for i in range(len(s)):
            if s[i] not in di:
                di[s[i]] = i
            else:
                j = max(j, di[s[i]] + 1)
                di[s[i]] = i
            max_l = max(max_l, i-j+1)
        return max_l