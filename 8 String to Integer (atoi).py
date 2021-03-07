# https://leetcode.com/problems/string-to-integer-atoi/


import re
class Solution:
    def myAtoi(self, s: str) -> int:
        a = '0'
        ni = 0
        if bool(re.match(r'^\s*[\+?|\-?]?\d+\w*',s)):
            for i in s:
                if i == '-' and ni == 0:
                    a='-'
                try:
                    int(i)
                    a+=i
                    ni = 1
                except:
                    if ni == 0:
                        continue
                    if ni == 1:
                        break
        return max(-2**31,min(int(a),2**31-1))