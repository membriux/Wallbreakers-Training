# Valid anagrams

'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        grams = {}
        for l in s:
            if l in grams:
                grams[l] += 1
            else:
                grams[l] = 1

        for l in t:
            if l in grams:
                grams[l] -= 1
                if grams[l] == 0:
                    grams.pop(l)
            else:
                grams[l] = 1

        return grams == {}
