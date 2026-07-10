class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        d = [1, 2]
        for i in range(2, n):
            d.append(d[-1]+d[-2])
        return d[-1]
        