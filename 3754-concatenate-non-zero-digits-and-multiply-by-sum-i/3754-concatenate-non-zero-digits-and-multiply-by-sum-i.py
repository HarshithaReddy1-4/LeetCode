class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        s = 0
        res = ''
        while n > 0:
            p = n % 10
            n = n // 10
            if p:
                res = str(p) + res
            s += p
        
        return s * int(res)


