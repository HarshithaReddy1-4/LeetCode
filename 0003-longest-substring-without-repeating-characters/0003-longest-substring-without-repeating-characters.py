class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        S = set()
        m = 0
        while j < len(s):
            if s[j] not in S:
                S.add(s[j])
                m = max(m, j - i + 1)
                j += 1
            else:
                S.remove(s[i])
                i += 1
        return m
        