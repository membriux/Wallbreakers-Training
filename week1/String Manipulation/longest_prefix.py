

# Longest Common Prefix
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
'''

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

            if len(strs) == 0 or len(strs[0]) == 0:
                return ""
            elif len(strs[0][0]) == 0:
                return ""
            if len(strs) == 1:
                return strs[0]

            res = ""
            l, w = 0, 0
            pre = strs[0][0]

            while w < len(strs):

                try:
                    if strs[w][l] != pre:
                        print(strs[w][l], "!=", strs[w][l])
                        return res

                    w += 1

                    if len(strs) == w:
                        res += pre
                        l += 1
                        w = 0
                        pre = strs[0][l]
                except:
                    return res
