class Solution:
    def reverseVowels(self, s: str) -> str:
        ss = list(s)
        v = set('aeiouAEIOU')
        n = len(s)
        i, j = 0, n - 1

        while i < j:
            if s[i] in v:
                while s[j] not in v:
                    j -= 1
                ss[i], ss[j] = ss[j], ss[i]
                j -= 1
            i += 1

        return ''.join(ss)
                
