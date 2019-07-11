'''
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        u = len(nums) - 1
        while l <= u:
            mid = (l+u) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < target:
                    l = mid + 1
                else:
                    u = mid - 1
        return -1
