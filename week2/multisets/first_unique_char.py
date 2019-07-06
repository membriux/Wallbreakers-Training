'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        found = False
        first = 1000000000
        for x in range(len(s)):
            if s[x] in chars:
                chars[s[x]].append(x)
            else:
                chars[s[x]] = [x]

        print(chars)
        for k,v in chars.items():
            if len(v) == 1:
                if v[0] <= first:
                    first = v[0]
                    print("new first:", first)
                    found = True
        if found:
            return first
        return -1
