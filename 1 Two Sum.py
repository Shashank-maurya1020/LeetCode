# https://leetcode.com/problems/two-sum/
'''
EXAMPLE:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

class Solution:
    def twoSum(self, nums, target):
        di = {nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            if target - nums[i] in di.keys() and i!=di[target - nums[i]]:
                return [i,di[target-nums[i]]]
a = Solution()
print(a.twoSum([2,7,11,15],9))