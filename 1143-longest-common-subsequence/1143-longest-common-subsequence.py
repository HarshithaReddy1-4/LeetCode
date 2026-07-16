class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # def lcs(i, j):
        #     if i < 0 or j < 0:
        #         return 0

        #     if text1[i] == text2[j]:
        #         return 1 + lcs(i - 1, j - 1)

        #     return max(lcs(i, j - 1), lcs(i - 1, j))
        
        # return lcs(len(text1) - 1, len(text2) - 1)
        n1 = len(text1) + 1
        n2 = len(text2) + 1
        dp = [[0] * n2 for _ in range(n1)]
        for i in range(1, n1):
            for j in range(1, n2):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
