class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        S = []
        m = 0
        for j in range(len(s)):
            while s[j] in S:
                S.remove(s[i])
                i += 1
            S.append(s[j])
            m = max(m, j - i + 1)
        return m
        