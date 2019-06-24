# Problem 2: Transpose Matrix

# Given matrix A, return transpose of A

# Transpose = matrix flipped over it's main diagonal,
# switching the row and column indices of the matrix

'''
Example: Input:
[[1,2,3],
 [4,5,6],
 [7,8,9]]

Output:
[[1,4,7],
 [2,5,8],
 [3,6,9]
]

Input
[[1,2,3],
 [4,5,6]]

Output
[[1,4],
 [2,5],
 [3,6]]
'''

class Solution:

    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        transpose = []
        for r in range(len(A[0])):
            temp = []
            for c in range(len(A)):
                temp.append(A[c][r])
            transpose.append(temp)
        return transpose
