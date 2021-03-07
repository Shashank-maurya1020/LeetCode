# https://leetcode.com/problems/longest-common-prefix/
'''
EXAMPLE

Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs == []:
            return ''
        low = strs[0]
        for i in strs:
            if len(i) < len(low):
                low = i
        str_ = ''
        for i in range(len(low)):
            for j in strs:
                if j[i] != low[i]:
                    return str_
            else:
                str_ += low[i]
        return str_


'''
Runtime: 72 ms, faster than 5.99% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.2 MB, less than 95.15% of Python3 online submissions for Longest Common Prefix.
'''