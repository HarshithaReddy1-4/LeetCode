class Solution:
    def minimumPushes(self, word: str) -> int:
        d = Counter(word)
        s = sorted(d, key = d.get, reverse = True)
        count = 0

        for i, ch in enumerate(s):
            push = i // 8 + 1
            count += d[ch] * push
        
        return count