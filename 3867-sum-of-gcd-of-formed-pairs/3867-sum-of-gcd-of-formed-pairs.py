class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        pref = []
        mx = float("-inf")

        for i in nums:
            mx = max(mx, i)
            pref.append(gcd(i, mx))
        
        pref.sort()
        summ = 0
        
        for i in range(len(pref)//2):
            summ += gcd(pref[-1 - i], pref[i])
        
        return summ
