# Single Number
'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dupl = {}
        for n in nums:
            if n in dupl:
                dupl.pop(n)
            else:
                dupl[n] = 1
        for i in dupl:
            return i
