# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_a = 0
        i = 0
        j = len(height)-1
        while i <= j:
            _ = min(height[i],height[j]) * abs(i-j)
            if _ > max_a:
                max_a = _
            if height[i] <= height[j]:
                i+=1
            else:
                j-=1
                
        return max_a