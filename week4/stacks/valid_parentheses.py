
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

'''

class Solution:
    def isValid(self, s: str) -> bool:

        valid = {'{': '}', '[': ']', '(': ')'}
        stack = []
        for p in s:
            if p in valid:
                stack.append(valid[p])
            else:
                if not stack or stack.pop() != p:
                    return False

        return True if not stack else False
