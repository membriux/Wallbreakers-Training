
'''
Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        num = 0

        while True:
            for x in str(n):
                num += int(x)**2

            if num == 1:
                return True

            elif num in seen:
                return False

            else:
                seen.add(num)
                num, n  = 0, num





                
