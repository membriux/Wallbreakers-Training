
"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        js = {}

        for s in S:
            if s in js:
                js[s] += 1
            else:
                js[s] = 1

        count = 0

        for j in J:
            if j in js:
                count += js[j]
        print("js:", js)

        return count
