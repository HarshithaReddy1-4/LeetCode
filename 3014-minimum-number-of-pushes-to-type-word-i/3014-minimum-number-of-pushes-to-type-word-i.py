class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n <= 8:
            return n
        
        count = 8
        n -= 8
        keys = 2
        c = 0
        for i in range(n):
            if c == 8:
                keys += 1
                c = 0
            count += keys
            c += 1
        return count

