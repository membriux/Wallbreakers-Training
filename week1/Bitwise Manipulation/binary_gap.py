# Binary gap
'''
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.



Example 1:

Input: 22
Output: 2
Explanation:
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.
'''


class Solution:
    def binaryGap(self, N: int) -> int:
        # convert N to binary and then to string
        n = list(bin(N)[2:])

        # Keep track of the index for all 1s
        ones = []
        for i in range(len(n)):
            if n[i] == '1':
                ones.append(i)
        # Keep track of longest distance
        dist = 0
        for i in range(len(ones)-1):
            if ones[i+1] - ones[i] > dist:
                dist = ones[i+1] - ones[i]
        return dist

        
