class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        i = 0
        d = {}
        m = 0

        for j in range(len(s)):
            d[s[j]] = d.get(s[j], 0) + 1
            while d[s[j]] > 2:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    del d[s[i]]
                i += 1
            m = max(m, j - i + 1)
            
        return m
        