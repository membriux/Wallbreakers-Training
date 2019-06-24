# Problem 3: Flip Image

'''

Given a binary matrix A, we want to flip the image horizontally, then invert it,
and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]


Input: [1,1,0]

revert row
[0,1,1]

Invert image
[1,0,0]

'''

class Solution:

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for r in range(len(A)):
            mid = len(A[r]) // 2
            # Revert row + invert image
            for c in range(len(A[r])):

                # Revert row
                if c < mid:
                    temp = A[r][c]
                    A[r][c] = A[r][-c-1]
                    A[r][-c-1] = temp

                # Invert image
                if A[r][c] == 0:
                    A[r][c] = 1
                else:
                    A[r][c] = 0
        return A
