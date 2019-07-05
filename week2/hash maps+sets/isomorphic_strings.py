'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso = dict()
        seen = set()
        for i in range(len(s)):

            if s[i] not in iso:
                if t[i] in seen:
                    return False
                iso[s[i]] = t[i]
                seen.add(t[i])

            elif iso[s[i]] != t[i]:
                return False

        print(iso)
        return True
