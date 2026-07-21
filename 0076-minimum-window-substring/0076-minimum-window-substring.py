class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}

        have = 0
        needCount = len(need)

        i = 0
        size = float('inf')
        left, right = -1, -1

        for j in range(len(s)):
            ch = s[j]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1
            
            while have == needCount:
                if size > j - i + 1:
                    size = j - i + 1
                    left, right = i, j
                
                window[s[i]] -= 1

                if s[i] in need and window[s[i]] < need[s[i]]:
                    have -= 1
                
                i += 1
            
        return s[left: right + 1]