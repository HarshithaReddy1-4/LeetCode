class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[0] * n for _ in  range(n)]
        suffix = piles[:]

        for i in range(n - 2, -1, -1):
            suffix[i] += suffix[i + 1]
        
        def func(i, m):
            if i + 2 * m >= n:
                return suffix[i]
            if dp[i][m] > 0:
                return dp[i][m]
            
            res = float("inf")
            for x in range(1, 2 * m + 1):
                res = min(res, func(i + x, max(m, x)))
            
            dp[i][m] = suffix[i] - res
            return dp[i][m]
        
        return func(0, 1)
