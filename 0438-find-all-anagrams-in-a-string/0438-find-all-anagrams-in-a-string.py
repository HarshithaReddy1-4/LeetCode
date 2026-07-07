class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        n = len(p)
        m = len(s)
        if n > m:
            return []
        res = []
        i = 0
        pd = Counter(p)
        d = {}
        for j in range(m):
            d[s[j]] = d.get(s[j], 0) + 1
            if j - i + 1 == n:
                if pd == d:
                    res.append(i)
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    del d[s[i]]
                i += 1
        return res


