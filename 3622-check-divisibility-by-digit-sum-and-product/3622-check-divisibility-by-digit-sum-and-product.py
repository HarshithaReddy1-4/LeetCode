class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ = 0
        prod = 1
        m = n

        while n > 0:
            p = n % 10
            summ += p
            prod *= p
            n = n // 10

        return False if m % (summ + prod) else True