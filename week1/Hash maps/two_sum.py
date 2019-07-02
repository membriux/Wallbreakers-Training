# Two sum

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [2, 3, 11, 15] target = 9
        subt = {}

        for n in range(len(nums)):
            if str(nums[n]) in subt:
                return [subt[str(nums[n])], n]

            if str(target - nums[n]) not in subt:
                subt[str(target - nums[n])] = n
        return





    
