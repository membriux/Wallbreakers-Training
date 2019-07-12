'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        groups = []
        res = []

        for i in range(len(s) - len(p) + 1):
            groups.append(s[i:i+len(p)])


        for i in range(len(groups)):
            if sorted(groups[i]) == sorted(p):
                res.append(i)

        return res
