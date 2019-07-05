

'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
'''

class Solution:
    def wordPattern(self, p: str, str: str) -> bool:
        if len(p) != len(str.split()):
            return False

        words = dict()
        seen = set()

        for i in range(len(p)):
            if str.split()[i] in words:
                if words[str.split()[i]] != p[i]:
                    return False

            if str.split()[i] not in words:
                if p[i] in seen:
                    return False
                words[str.split()[i]] = p[i]
                seen.add(p[i])

        print(words)
        return True
        
