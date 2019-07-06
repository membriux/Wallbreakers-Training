class Solution:

    def make_dict(self, p):
        d = {}
        for x in p:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        return d


    def compare(self, s_dict, p_dict):
        return s_dict == p_dict

                
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = {}
        p_dict = self.make_dict(p)
        for i in range(0, len(s) - len(p)):
            if s[i] in p:
                s_dict = self.make_dict(s[i:i+len(p)])
                if self.compare(s_dict, p_dict):
                    res[i] = s[i:i+len(p)]

        last = self.make_dict(s[len(s)-len(p):len(s)])
        if self.compare(last, p_dict):
            res[len(s) - len(p)] = s[len(s) -len(p): len(s)]

        print(res)
        return list(res)
