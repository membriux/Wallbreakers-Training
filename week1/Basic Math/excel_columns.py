# Problem 4: Excel column numbers
'''

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        return sum( (ord(c) - 64) * 26 ** (len(s) - idx - 1) for idx, c in enumerate(s) )
