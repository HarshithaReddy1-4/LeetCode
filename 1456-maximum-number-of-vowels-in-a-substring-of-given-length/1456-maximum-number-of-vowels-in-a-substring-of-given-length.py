class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i, c, m = 0, 0, 0

        for j in range(len(s)):
            if s[j] in 'aeiou':
                c += 1
            if j - i + 1 == k:
                m = max(m, c)
                if s[i] in 'aeiou':
                    c -= 1
                i += 1
            
        return m