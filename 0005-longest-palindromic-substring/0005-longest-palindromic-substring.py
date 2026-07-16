class Solution:
    def longestPalindrome(self, s: str) -> str:
        # ans = ''
        # def func(s):
        #     nonlocal ans
        #     if len(s) <= 0:
        #         return
        #     for i in range(len(s)):
        #         a = s[:i + 1]
        #         if a == a[::-1] and len(a) > len(ans):
        #             ans = a
        #     func(s[1:])
        # func(s)
        # return ans
        # res = ''

        # def check(l, r):
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         l -= 1
        #         r += 1
        #     return s[l + 1: r]

        # for i in range(len(s)):
        #     x = check(i, i)
        #     y = check(i, i + 1)
        #     res = max(res, x, y, key = len)

        # return res

        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        start = 0
        maxx = 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                start = i
                maxx = 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                    dp[i][j] = 1
                    start = i
                    maxx = length

        return s[start: start + maxx]