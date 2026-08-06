class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        m = n
        for _ in range(10):
            prod = 1
            temp = m
            while temp > 0:
                p = temp % 10
                prod *= p
                temp = temp // 10
            if prod % t == 0:
                return m
            m += 1

            