# Problem 3: Reverse string iii

'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        rev = ""
        for word in s.split():
            rev += word[::-1] + " "
        return rev[:-1]
