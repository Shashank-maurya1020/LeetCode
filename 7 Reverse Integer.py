# https://leetcode.com/problems/reverse-integer/
'''
Example

Input: x = 123
Output: 321
'''

class Solution:
    def reverse(self, x: int) -> int:
        s = 0
        temp = 1 if x >= 0 else -1
        x = abs(x)
        while x!=0:
            s = s*10 + x%10
            x//=10
        if s in range(-2**31, 2**31 - 1):
            return s * temp
        return 0
        
'''
Runtime: 20 ms, faster than 99.53% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.3 MB, less than 13.43% of Python3 online submissions for Reverse Integer
'''