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
