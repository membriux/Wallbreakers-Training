
# Hamming Distance

'''
The Hamming distance between two integers is the number of
positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        x = format(x, '#033b')
        y = format(y, '#033b')
        for i in range(len(x)):
            if x[i] != y[i]:
                res += 1

        return res
