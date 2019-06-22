# Leetcode solutions for problems regarding Arrays:



# Problem 1: Sort array by Parity
# Given an array A of non-negative integers,
# return an array consisting of all the even
# elements of A, followed by all the odd elements of A.


# Example:
# Input: [3,1,2,4] ––> output: [2,4,3,1]

class Solution:

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evens = list()
        odds = list()

        for num in A:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)

        return evens + odds

    def betterSolution(self, A: List[int]) -> List[int]:
        A.sort(key = lambda x: x % 2)
        return A


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













# Problem 3


















# Problem 4










# Problem 5
