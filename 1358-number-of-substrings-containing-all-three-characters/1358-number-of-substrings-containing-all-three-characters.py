class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = {'a': 0, 'b': 0, 'c': 0}
        i = 0
        n = len(s)
        ans = 0

        for j in range(n):
            d[s[j]] += 1

            while d['a'] >= 1 and d['b'] >= 1 and d['c'] >= 1:
                ans += (n - j)
                d[s[i]] -= 1
                i += 1
        return ans
