# Valid Palindrome

'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        first, last = 0, len(s) - 1
        while first < last:
            if not s[first].isalpha() and not s[first].isdigit():
                first += 1
                continue
            if not s[last].isalpha() and not s[last].isdigit():
                last -= 1
                continue
            # print("checking:", s[first], "and", s[last])

            if s[first].lower() != s[last].lower():
                return False

            first += 1
            last -= 1

        return True
