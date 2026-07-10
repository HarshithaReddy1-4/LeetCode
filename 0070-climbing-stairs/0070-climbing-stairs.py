class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev1, prev2 = 2, 1
        for i in range(2, n):
            prev1, prev2 = prev1 + prev2, prev1
        return prev1
        