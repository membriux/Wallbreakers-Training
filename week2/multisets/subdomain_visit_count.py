
'''
For this problem, I would get the correct values returned.
However, it wouldn't return them in the same order that the leetcode
solution has it. I tried multiple test cases and it works like a charm.
'''
class Solution:
    def subdomainVisits(self, domains: List[str]) -> List[str]:
        doms = dict()

        for s in domains:
            cnt = s.split()[0]
            dom = s.split()[1].split('.')
            subs = []
            for d in range(len(dom)):
                subs.append(".".join(s for s in dom[d:]))
            # print(subs)

            # print(dom)
            for sub in subs:

                if sub in doms:
                    doms[sub] += int(cnt)
                else:
                    doms[sub] = int(cnt)
        # print(doms)

        return [str(v) + " " + k for k,v in doms.items()]
