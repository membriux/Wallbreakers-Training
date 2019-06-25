# Problem 5: Power of twos

'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
'''


class Solution:


    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while 2**i <= n:
            if 2**i == n:
                return True
            i += 1

        return False
