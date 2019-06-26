
# Reverse Vowels

'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
'''

class Solution:

    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u'}
        res = ''
        to_change = []
        for i in range(len(s)):
            if s[i].lower() in vowels:
                to_change.append(s[i])

        for c in range(len(s)):
            if s[c].lower() in vowels:
                res += to_change.pop()
            else:
                res += s[c]
        return res


        
