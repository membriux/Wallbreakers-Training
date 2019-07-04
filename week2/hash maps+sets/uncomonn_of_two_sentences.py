'''
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

'''

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        unc = dict()

        for word in A.split():
            if word not in unc:
                unc[word] = 1
            else:
                unc[word] += 1

        for word in B.split():
            if word in unc:
                unc[word] += 1
            else:
                unc[word] = 1

        return [w for w in unc if unc[w] == 1]




            
