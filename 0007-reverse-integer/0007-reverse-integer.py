class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        neg = False
        if x < 0:
            x = -x
            neg = True

        while x > 0:
            p = x % 10
            num = num * 10 + p
            x = x// 10

        if neg:
            num = -num
        
        if num < -2**31 or num > (2**31) - 1:
            return 0

        return num