class Solution:
    def reverseVowels(self, s: str) -> str:
        ss = [i for i in s]
        n = len(s)
        i, j = 0, n - 1

        while i < j:
            if s[i] in 'aeiouAEIOU':
                while s[j] not in 'aeiouAEIOU':
                    j -= 1
                ss[i], ss[j] = ss[j], ss[i]
                j -= 1
            i += 1
            
        return ''.join(ss)
                
