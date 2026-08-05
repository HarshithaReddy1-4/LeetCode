class Solution:
    def reverseVowels(self, s: str) -> str:
        s1 = s[::-1]
        ss = [i for i in s]
        n = len(s)
        i, j = 0, 0

        while i < n and j < n:
            if ss[i] in 'aeiouAIEOU':
                while s1[j] not in 'aeiouAEIOU':
                    j += 1
                ss[i] = s1[j]
                j += 1
            i += 1
        return ''.join(ss)
                
                
