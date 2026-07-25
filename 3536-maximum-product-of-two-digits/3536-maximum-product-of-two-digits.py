class Solution:
    def maxProduct(self, n: int) -> int:
        s = list()
        n = str(n)
        for i in n:
            s.append(int(i))
            
        s.sort()
        return s[-1] * s[-2]