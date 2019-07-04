
'''
You are given an array A of strings.

Two strings S and T are special-equivalent if after any number of moves, S == T.

A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping S[i] with S[j].

Now, a group of special-equivalent strings from A is a non-empty subset S of A such that any string not in S is not special-equivalent with any string in S.

Return the number of groups of special-equivalent strings from A.
'''

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        res = set()
        for item in A:
            odds = item[::2]
            evens = item[1::2]
            res.add((str(sorted(odds)),str(sorted(evens))))
        print(res)
        return len(res)
